#!/usr/bin/env python
import sys
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    sys.path.insert(0, '.')
    execute_from_command_line(sys.argv)
