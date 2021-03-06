# -*- coding: utf8 -*-
# Copyright (c) 2019 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""
`pydoc_markdown.interfaces`
===========================

This module defines the interfaces that can to be implemented for
Pydoc-Markdown to implement custom loaders for documentation data,
processors or renderers.
"""

from nr.databind.core import  SerializeAs, UnionType
from nr.interface import Interface, default
from typing import Optional
from .reflection import ModuleGraph, Object
import subprocess


@SerializeAs(UnionType.with_entrypoint_resolver('pydoc_markdown.interfaces.Loader'))
class Loader(Interface):
  """
  This interface describes an object that is capable of loading documentation
  data. The location from which the documentation is loaded must be defined
  with the configuration class.
  """

  def load(self, graph):  # type: (ModuleGraph) -> None
    """
    Fill the #ModuleGraph.
    """


class LoaderError(Exception):
  pass


@SerializeAs(UnionType.with_entrypoint_resolver('pydoc_markdown.interfaces.Processor'))
class Processor(Interface):
  """
  A processor is an object that takes a #ModuleGraph object as an input and
  transforms it in an arbitrary way. This usually processes docstrings to
  convert from various documentation syntaxes to plain Markdown.
  """

  def process(self, graph, resolver):  # type: (ModuleGraph, Optional[Resolver]) -> None
    pass


class Resolver(Interface):
  """ A resolver can be used by a #Processor to replace cross references
  with a hyperlink. """

  def resolve_ref(self, scope: Object, ref: str) -> Optional[str]:
    pass


@SerializeAs(UnionType.with_entrypoint_resolver('pydoc_markdown.interfaces.Renderer'))
class Renderer(Processor):
  """
  A renderer is an object that takes a #ModuleGraph as an input and produces
  output files or writes to stdout. It may also expose additional command-line
  arguments. There can only be one renderer at the end of the processor chain.

  Note that sometimes a renderer may need to perform some processing before
  the render step. To keep the possibility open that a renderer may implement
  generic processing that could be used without the actual renderering
  functionality, #Renderer is a subclass of #Processor.
  """

  @default
  def process(self, graph, resolver):  # type: (ModuleGraph, Optional[Resolver]) -> None
    pass

  def render(self, graph):  # type: (ModuleGraph) -> None
    pass

  def get_resolver(self, graph):  # type: (ModuleGraph) -> Optional[Resolver]
    pass


class Server(Interface):
  """
  This interface describes an object that can start a server process for
  live-viewing generated documentation in the browser. #Renderer
  implementations may additionally implement this interface to advocate their
  compatibility with the `--server` and `--open` options of the pydoc-markdown
  CLI.
  """

  def get_server_url(self) -> str:
    ...

  def start_server(self) -> subprocess.Popen:
    ...

  @default
  def reload_server(self, process: subprocess.Popen) -> subprocess.Popen:
    """
    Called when the files generated by pydoc-markdown have been updated.
    This gives the implementation a chance to reload the server process.
    The default implementation returns the *process* unchanged. Returning
    #None will automatically call #start_server() afterwards.
    """

    return process
