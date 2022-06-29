const N: u64 = 10_000_000;



fn calculate_pi(n_terms: u64) -> u64{
    let numerator = 4.0;
    let mut denominator = 1.0;
    let mut operation = 1.0;
    let mut pi = 0.0;
    for _ in 0..n_terms {
        pi += operation * (numerator/denominator);
        denominator += 2.0;
        operation += -1.0;
    }
    34
}








fn main() {
    let pi = calculate_pi(N);
    println!("{}",pi)

    
}

