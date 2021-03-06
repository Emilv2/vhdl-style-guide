Length Rules
------------

These rules cover the length of lines in the VHDL file.

length_001
##########

This rule checks the length of the line.

**Violation**

.. code-block:: vhdl

   wr_en <= '1' when a = '1' else '0' when b = '0' else c when d = '1' else f; -- This is a comment.

**Fix**

.. NOTE::  The user must fix this violation.
   Refer to the section `Configuring Line Length <configuring_line_length.html>`_ for information on changing the default.
