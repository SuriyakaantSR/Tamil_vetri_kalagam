use std::io; // converting fahrenheit to celsius
fn main() {
    loop {
        println!("What do you want to convert ? ");
        println!("1. Fahrenheit to Celsius");
        println!("2. Celsius to Fahrenheit");
        // add an condition to convert to celsius
        let mut choice = String::new();
        io::stdin()
            .read_line(&mut choice)
            .expect("an error occurred");

        let choice: u32 = match choice.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        if choice > 2 {
            println!("Invalid choice! Please try again.");
            return;
        }

        if choice == 1 {
            println!("Enter the fahrenheit : ");
            let mut f = String::new();

            io::stdin().read_line(&mut f).expect("an error occurred");

            let f: f64 = match f.trim().parse() {
                Ok(num) => num,
                Err(_) => continue,
            };

            let c: f64 = convert_fahrenheit(f);
            println!("celsius : {}", c);
        } else if choice == 2 {
            println!("Enter the celsius : ");
            let mut c = String::new();
            io::stdin().read_line(&mut c).expect("an error occurred");

            let c: f64 = match c.trim().parse() {
                Ok(num) => num,
                Err(_) => continue,
            };
            let f: f64 = convert_celsius(c);
            println!("fahrenheit : {}", f);
        } else {
            println!("Invalid choice! Please try again.");
        }
    }
}

// convert fahrenheit to celsius

fn convert_fahrenheit(f: f64) -> f64 {
    (f - 32.0) * 5.0 / 9.0
}

fn convert_celsius(c: f64) -> f64 {
    (c * 5.0 / 9.0) + 32.0
}
