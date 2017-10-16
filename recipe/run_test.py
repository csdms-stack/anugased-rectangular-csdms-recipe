#! /usr/bin/env python
import os
from pymt.components import AnugaSedRectangular


os.mkdir('_testing')
os.chdir('_testing')

component = AnugaSedRectangular()
component.get_component_name()
component.setup('.')
component.initialize('anuga.yaml')
component.update()
component.finalize()
