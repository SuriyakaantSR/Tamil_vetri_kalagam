
fn main () {

    // using the for loop to print the first 10 fibonacci numbers 

    for n in 0..10 {
    let fib = fib_num(n);
    println!("{}", fib);
    }
}


fn fib_num (n:u32) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        _ => fib_num(n-1) + fib_num(n-2)
    }
}