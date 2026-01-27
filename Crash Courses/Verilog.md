# $\fbox{VERILOG}$





## **Topic - 1: Digital Logic Fundamentals**

### <u>Combinational Logic</u>

- AND gate
- OR gate
- Adders
- Multiplexers


### <u>Sequential Logic</u>

- Flip-flop
- Registers
- Counters
- FSMs


### <u>Clock</u>

- **<u>Clock</u>:** Repeating square wave from $0 \rightarrow 1$ and $1 \rightarrow 0$.

```verilog
always @(posedge clk)
```


### <u>About Verilog</u>

- Verilog doesn't draw circuit, but define hardware behavior.
- Unlike software code which executes in steps, whole hardware exists parallelly.

```verilog
assign y = a & b
```


### <u>Field Programmable Gate Array</u>

- **FPGA components -** Logic blocks (LUTs), flip-flops, interconnects, clock networks.
- Verilog $\rightarrow$ Synthesis $\rightarrow$ FPGA hardware



## **Topic - 2: Verilog Basics**

### <u>Basic Structure</u>

- **<u>Modules</u>:** Hardware blocks

```verilog
module module_name (
	input a;
	input b;
	output y
);

/* Hardware description */

endmodule
```


### <u>Wire</u>

- **<u>Wire</u>:** A physical connection in combinational logic.
- Connection is made using `assign`.

```verilog
wire y;
assign y = a & b;
```


### <u>Reg</u>

- **<u>Reg</u>:** Stores a value temporarily in sequential logic.
- Used inside `always` blocks only.

```verilog
reg y;
```


### <u>Continuous Assignment</u>

```verilog
assign y = a & b;        // a AND b
```


### <u>Testbench Steps</u>

1. Timescale
2. Testbench module name
3. Components declaration
4. Unit under test
5. Dump file name
6. Dump variables
7. Initial values

```verilog
`timescale 1ns/1ps

module testbench;

    reg a, b;
    wire y;

    and_gate uut (        // Unit under test
        .a(a),
        .b(b),
        .y(y)
    );

    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, tb_and_gate);

        a = 0; b = 0; #10;        // 10 = Time to pause for
        a = 0; b = 1; #10;
        a = 1; b = 0; #10;
        a = 1; b = 1; #10;

        $finish;
    end

endmodule
```


### <u>Related Shell Command</u>

#### Compilation:

```sh
iverilog -o my_circuit my_circuit.v testbench.v
```

#### Running simulation:

```sh
vvp my_circuit
```

#### Wave monitoring:

```sh
gtkwave wave.vcd
```



## **Topic - 3: Combinational Circuits**

### <u>Using Always</u>

- `assign` is used for simple expressions.
- While `always @(*)` is used for decision based logic.
- Forgetting to write `@(*)` might accidentally create latches.

```verilog
always @(*) begin
    if (a == 1'b0)
        y = b;
    else
        y = c;
end
```



## **Topic - 4: Block Assignments**

### <u>Use Of Always</u>

- Using `always` means the logic inside `always` will be re-evaluated.
- `@(*)` means all inputs are re-evaluated.
- Inside `always` block, only `reg` values are updated, procedurally.

| Assignment Type | Meaning      | Purpose                                                      |
| :-------------: | :----------- | :----------------------------------------------------------- |
|       `=`       | Blocking     | To execute in order, for values to be updated for next line. |
|      `<=`       | Non-blocking | Unordered execution when using a clock.                      |


### <u>Full Adder</u>

```verilog
module full_adder(
    input  a,
    input  b,
    input  cin,
    output reg sum,
    output reg cout
);

always @(*) begin
    sum  = a ^ b ^ cin;
    cout = (a & b) | (cin & (a ^ b));
end

endmodule
```



## **Topic - 5: Control Statements**

### <u>Conditional Statements</u>

```verilog
always @(*) begin
    if (sel == 0)
        y = a;        // y is reg
    else
        y = b;
end
```

- `y` have to a `reg` to work inside `always` block.


### <u>Multi-Bit Vector</u>

```verilog
input [1:0] in,
output reg [3:0] y
```

- `in` is of 2-bits & `y` of `4`.
- Used in multiplexers, demultiplexers, etc.


### <u>Switch-Cases</u>

```verilog
case (in)
    2'b00: y = 4'b0001;
    2'b01: y = 4'b0010;
    2'b10: y = 4'b0100;
    2'b11: y = 4'b1000;
    default: y = 4'b0000;
endcase
```

- `2'b00` = `2`-bit binary (`b`) valued `00`.
- `4'b0000` = `4`-bit binary (`b`) valued `0000`.


### <u>Example Codes</u>

#### Multiplexer:

```verilog
module mux2to1(
    input  a,
    input  b,
    input  sel,
    output reg y
);

always @(*) begin
    if (sel == 0)
        y = a;
    else
        y = b;
end

endmodule
```

#### Decoder code:

```verilog
module decoder2to4(
    input  [1:0] in,
    output reg [3:0] y
);

always @(*) begin
    case (in)
        2'b00: y = 4'b0001;
        2'b01: y = 4'b0010;
        2'b10: y = 4'b0100;
        2'b11: y = 4'b1000;
        default: y = 4'b0000;
    endcase
end

endmodule
```



## **Topic - 6: Sequential Logic & Clocks**

### <u>Clock Condition</u>

```verilog
always @(posedge clk) begin
	q <= d;
end
```

- Now values inside `always` block update only during clock edges.
- And we use `<=` for sequential circuits.


### <u>Testbench Changes</u>

```verilog
`timescale 1ns/1ps

module tb_dff;
	
    reg clk;
    reg rst;
    reg d;
    wire q;
	
    dff uut (.clk(clk), .rst(rst), .d(d), .q(q));
	
    always #5 clk = ~clk;        // ADDED LINE: 10 ns period for clock
	
    initial begin
	    $dumpfile("wave.vcd");
        $dumpvars(0, tb_dff);
        
        clk = 0; rst = 1; d = 0; #12
        rst = 0;        // Release reset (not on edge)
		
        d = 1;  #10;        // Sampled on next posedge
        d = 0;  #10;
        d = 1;  #10;
		
        $finish;
    end
	
endmodule
```
