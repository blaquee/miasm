#! /usr/bin/env python
from asm_test import Asm_Test
import sys

class Test_PSHUFB(Asm_Test):
    TXT = '''
    main:
       CALL   next
       .byte 0x88, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11
       .byte 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0
    next:
       POP    EBP
       MOVQ   MM0, QWORD PTR [EBP]
       MOVQ   MM1, MM0
       PSHUFB MM1, QWORD PTR [EBP+0x8]
       RET
    '''

    def check(self):
        assert self.myjit.cpu.MM0 == 0x1122334455667788L
        assert self.myjit.cpu.MM1 == 0x8877665544332211L


if __name__ == "__main__":
    [test()() for test in [Test_PSHUFB]]
