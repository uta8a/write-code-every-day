use std::fs;
struct Expr {
  ret: i64,
}


fn eval(input: String) -> String {
  let expr = Expr{ret: 0};
  for ch in input.chars() {
    if ch == '+' {
      
    }
    let num = ch as i32 - 48;
    if 0<= num && num <= 9  {
      
    }
  }
  input
}
fn main() -> Result<(), Box<std::error::Error>> {
  let content = fs::read_to_string("./input.lang")?;
  println!("{}", eval(content));
  Ok(())
}

/*
add only calc
*/
