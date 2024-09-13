
fn main () {
    let fib = fib_num(8);
    println!("{}", fib);
}


fn fib_num (n:u32) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        _ => fib_num(n-1) + fib_num(n-2)
    }
}