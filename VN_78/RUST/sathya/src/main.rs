
use std::io;
use rand::Rng;

fn main(){
    println!("Guess the Number !");
    println!("Input ur Guess");

    let mut guess = String::new();

    io::stdin()
    .read_line(&mut guess)
    .expect("An error occurred");

    println!("Ur Guess is : {}", guess);

}