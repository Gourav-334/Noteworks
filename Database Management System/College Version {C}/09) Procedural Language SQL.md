# $\fbox{Chapter 9: PROCEDURAL LANGUAGE SQL}$





## **Topic - 1: Basics**

### <u>Basics</u>

- One of the three Oracle embedded languages.
- PL/SQL is portable, high-performing and OS independent.
- Can be called from cmd.


### <u>Features</u>

- Integrated with SQL.
- Error debugging feature.
- Many data type.
- Supports functions.
- Supports OOP.
- Can make web applications and servers.


### <u>Advantages</u>

- Supports both static & dynamic SQL.
- Static supports DML & dynamic supports DDL.
- Error debugging feature.
- High performance.


### <u>Syntax Format</u>

- `DECLARE`
- `BEGIN`
- `EXCEPTION` (*optional*)
- `END`


### <u>Basic Syntax</u>

```plsql
DECLARE
message varchar2^{20} := 'Hello, World!';

BEGIN
dbms_output.put_line(message);
END;

--single line comment

/* multiline comment */
```


### <u>About Syntax</u>

- Identifier must not exceed 30 characters.
- Reserved words are also identifiers.
- Storage location is allotted as per variable name.
- Some data types include integer, real, number etc.
- If a `DECLARE` block is declared before `BEGIN` block, then it contains global variables.
- And `DECLARE` block after `BEGIN` block contains local variable.
- You can write SQL commands in PL/SQL.


### <u>Value Output</u>

```plsql
dbms_output.put_line('Value of x is: ' || x);
```


### <u>Cursor</u>

- A cursor is used for selecting rows.

#### Cursor types:

  - **<u>Implicit</u>:** Automatic and predefined.
  - **<u>Explicit</u>:** User defined and called manually.


### <u>Cursor Keywords</u>

- `%FOUND`
- `%NOTFOUND`
- `%ISOPEN`
- `%ROWCOUNT`


### <u>Cursor Example</u>

```plsql
IF sql%FOUND THEN
--codes

ELSEIF sql%NOTFOUND THEN
--more codes

ENDIF;
```


### <u>Creating Explicit Cursor</u>

```plsql
CURSOR cursor_name IS select_statement;

OPEN cursor_name;           --opening it
CLOSE cursor_name;

FETCH name,id;              --to fetch

EXIT WHEN c%NOTFOUND        --to exit while searching
```


### <u>Loops</u>

```plsql
LOOP
--codes
END LOOP;
```


### <u>Triggers</u>

- Programs that execute automatically.

#### Advantages:

  - Write literally anything.


### <u>Trigger Syntax</u>

```plsql
CREATE TRIGGER trigger_name;
REPLACE TRIGGER trigger_name;
--BEFORE/ AFTER/ WHEN/ INSTEAD OF for setting trigger condition
```


### <u>Stored Procedure</u>

- Function
- Contains two parts - Header & Body


### <u>Syntax for Stored Procedure</u>

```plsql
CREATE PROCEDURE proc_name
AS
--codes (add BEGIN, END etc)

GO
DROP PROCEDURE proc_name
```


### <u>About Stored Procedured</u>

- `RETURN` statement does exist in PL/SQL stored procedures.

 
---
