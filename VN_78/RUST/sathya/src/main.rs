
use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main(){
    println!("Guess the Number !");

    let secret_num = rand::thread_rng()
                    .gen_range(1..=100);
    loop {
        
        println!("Input ur Guess");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect(" An error occurred ! ");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num ,
            Err(_) => continue ,
        };

        println!(" Ur Guess is {guess} ");

        match guess.cmp(&secret_num) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal =>{ println!("You guessed it right!"); break; }
            }
    }
}