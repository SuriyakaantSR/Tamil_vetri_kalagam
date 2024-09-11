
use std::io;

// converting fahrenheit to celsius
fn main() {
	loop{
	println!("Enter the fahrenheit : ");

	let mut f = String::new();  

	io::stdin()
		.read_line(&mut f)
		.expect("an error occurred");

	let f: f64 = match f.trim().parse() {
		Ok(num) => num,
		Err(_) => continue , 
	};

	let c :f64 = convert_fahrenheit(f);
	println!("celcius : {}", c);
	}
}

// convert fahrenheit to celsius

fn convert_fahrenheit(f: f64) -> f64 {
		(f-32.0)*5.0/9.0 
}

