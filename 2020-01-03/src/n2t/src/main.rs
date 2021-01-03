pub fn nand(a: bool, b: bool) -> bool {
    !(a && b)
}
pub fn not(a: bool) -> bool {
  nand(a,a)
}
pub fn and(a: bool, b: bool) -> bool {
  not(nand(a,b))
}
pub fn or(a: bool, b: bool) -> bool {
  nand(not(a), not(b))
}
pub fn mux(a: bool, b: bool, sel: bool) -> bool {
  or(and(a, not(sel)), and(b, sel))
}


pub struct Flipflop {bit: bool}
impl Flipflop {
  pub fn new() -> Self {
    Self {bit: false}
  }
  pub fn out(&self) -> bool {
    self.bit
  }
  pub fn clock(&mut self, a: bool) {
    self.bit = a;
  }
}
pub struct BitRegister {flipflop: Flipflop}
impl BitRegister {
  pub fn new() -> Self{
    Self{flipflop: Flipflop::new()}
  }
  pub fn out(&self) -> bool {
    self.flipflop.out()
  }
  pub fn clock(&mut self, input: bool, load: bool) {
    self.flipflop.clock(mux(self.out(), input, load))
  }
}
fn main(){}
#[test]
fn test_reg() {
  let mut register = BitRegister::new();
  let inputs = [
    (true, true),
    (true, false),
    (false, true),
    (false, false),
  ];
  let mut prev = register.out();
  for &(input, load) in &inputs {
    register.clock(input, load);
    assert_eq!(register.out(), if load {input} else{prev});
    prev = register.out();
  }
}
