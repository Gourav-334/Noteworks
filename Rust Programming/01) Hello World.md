# $\fbox{Chapter 1: HELLO WORLD}$





## **Topic - 1: Hello World**

### <u>Introduction</u>

- `println!` is a macro.
- We create an executable from Rust source using `rustc` command.

```sh
rustc hello.rs
./hello
```


### <u>Comment</u>

#### Regular comment:

- **<u>Line comment</u>:** Single-line, written with `//`.
- **<u>Block comments</u>:** Multi-line, written with `/**/`.

#### Doc comments:

- **<u>Following item</u>:** `///`
- **<u>Enclosed item</u>:** `//!`


### <u>Formatting Macros</u>

#### About:

- Present in `std::fmt`.
- We will explore specifically `fmt::Display`.
- `fmt::Debug` module uses `{:?}` very often.

#### Macros:

- `format!` - Formats string.
- `print!` - Formats string & prints it to console.
- `println!` - Formats string, adds newline & prints it to console.
- `eprint!` - Formats string & prints it as error.
- `eprintln!` - Formats string, adds newline & prints it as error.


### <u>Printing Methods</u>

#### Ways to print:

```rust
/* Single argument */
println!("Date: {}", 24);

/* Positional arguments (Its a special date below!) */
println!("Date: {0}, Month: {1}, Year: {2}", 24, 4, 2025);

/* Named arguments */
println!("Date: {date}, Month: {month}", date=24, month=2025);
```

#### Base conversions:

```rust
println!("Decimal: {}", 30);
println!("Binary: {:b}", 30);
println!("Octal: {:o}", 30);
println!("Hexadecimal: {:x}", 30);
```

#### Justification & padding:

```rust
println!("{num:<5}", num=7);           // Four spaces & then 7.
println!("{num:>5}", num=7);           // 7 & then four spaces.

println!("{num:0<5}", num=7);          // Four 0 & then 7.
println!("{num:0>5}", num=7);          // 7 & then four 0.

println!("{num:0<x$}", num=7, x=5);    // 'x' 0 & then 7.
```
