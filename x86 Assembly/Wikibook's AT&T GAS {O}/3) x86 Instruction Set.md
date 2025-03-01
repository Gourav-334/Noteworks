# $\fbox{Chapter 2: x86 INSTRUCTION SET}$





## **Topic - 1: Summary**

- Data transfer instructions
- Control flow instructions
- Arithmetic instructions
- Logic instructions
- Shift & rotate instructions
- Other instructions
- x86 interrupts



## **Topic - 2: Conventions**

### <u>Templates</u>

- **<u>Argument</u>:** The operand in instructions requiring single operand.
- **<u>Auxiliary operand</u>:** Third operand in instructions requiring three operands.

```asm
instr aux, src, dest        # AT&T syntax
instr dest, src, aux        ; Intel syntax
```


### <u>Suffixes</u>

- `b` - Byte (8-bits)
- `w` - Word (16-bits)
- `l` - Long/doubleword (32-bits)
- `q` - Quadword (64-bits)



## **Topic - 3: Data Transfer**
