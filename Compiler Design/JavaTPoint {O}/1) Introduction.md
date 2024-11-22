# <u>Chapter 1</u>: INTRODUCTION





## **Topic – 1: Compiler Introduction**

### <u>Introduction</u>

- **<u>Compiler</u>:** A translator that converts high-level language into machine language.
- High-level language is often referred as HLL & low-level language as LLL.
- **<u>Object program</u>:** Low-level language, like assembly.

$$ \xrightarrow{Source \; Prograrm} \framebox[3cm][c]{Compiler} \; \xrightarrow{Object \; Program} $$
$$ \xrightarrow{Object \; Prograrm} \framebox[3cm][c]{Assembler} \; \xrightarrow{Target \; Program} $$


### <u>Expected Topics To Be Covered</u>

- Introduction
- Grammar
- Parsing
- Syntax directed translation
- Symbol table
- Course optimization
- Code generation



## **Topic – 2: Compiler Phases**

### <u>Introduction</u>

$$ \framebox[8cm][c]{1) Source Program} $$
$$ \downarrow $$
$$ \framebox[8cm][c]{2) Lexical Analyzer} $$
$$ \downarrow $$
$$ \framebox[8cm][c]{3) Syntax Analyzer} $$
$$ \downarrow $$
$$ \framebox[8cm][c]{4) Semantic Analyzer} $$
$$ \downarrow $$
$$ \framebox[8cm][c]{5) Intermediate Code Generator} $$
$$ \downarrow $$
$$ \framebox[8cm][c]{6) Code Optimization} $$
$$ \downarrow $$
$$ \framebox[8cm][c]{7) Code Generator} $$
$$ \downarrow $$
$$ \framebox[8cm][c]{8) Target Program} $$


### <u>Lexical Analysis</u>

- Analyses source program character-by-character.
- Converts program into meaningful ***lexemes***.
- **Lexemes** are represented in form of tokens.

$$ Sum \; := \; (Old \; sum) \; + \; (Rate*50) $$
$$ \downarrow $$
$$ \framebox[7cm][c]{Lexical Analyzer} $$
$$ \downarrow $$
$$ id1 \; = \; id2 \; + \; (id3*id4) $$


### <u>Syntax Analysis</u>

- Takes tokens (lexemes) as input.
- Converts it into a parse tree.
- Then parser checks if the syntax is written the right way or not.

![Syntax Analyzer](./media/image3.png)


### <u>Semantic Analysis</u>

- In this phase, it checks if parse tree follows language rules or not.
- Then it tracks all involved identifiers, their types & the expression.

![Semantic Analysis](./media/image4.png)


### <u>Intermediate Code Generation</u>

- Code which is later converted into final machine code.

$$ \downarrow $$
$$ \framebox[7cm][c]{Intermediate Code Generator} $$
$$ \downarrow$$
$$ temp1 \; := \; inttoreal(50) $$
$$ temp2 \; := \; id3*temp1 $$
$$ temp3 \; := \; id2*temp2 $$
$$ id1 \; := \; temp3 $$


### <u>Code Optimization (*Optional)</u>

- Converting intermediate code in a form that will run faster & take less space.
- Like removing unnecessary lines, arranging code lines in an order etc.

$$ \downarrow $$
$$ \framebox[7cm][c]{Code Optimization} $$
$$ \downarrow $$
$$ temp1 \; := \; id3*50.0 $$
$$ id1 \; := \; id2 \; + \; temp1 $$


### <u>Code Generation</u>

- Takes the optimized intermediate code or just intermediate code as input.
- Converts that into processor’s machine code.

$$ \downarrow $$
$$ \framebox[7cm][c]{Code Generation} $$
$$ \downarrow $$
$$ MOVF \; id3, \; R2 $$
$$ MULF \; \#50.0, \; R2 $$
$$ MOVF \; id2, \; R2 $$
$$ ADDF \; R2, \; R1 $$
$$ MOVF \; R1, \; id1 $$
