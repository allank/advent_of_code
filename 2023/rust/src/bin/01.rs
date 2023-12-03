fn main() {
    let input: &str = include_str!("input_01.txt").trim();
    // let input: &str = "two1nine
// eightwothree
// abcone2threexyz
// xtwone3four
// 4nineeightseven2
// zoneight234
// 7pqrstsixteen";

    // let answer_01 = part_01(&input);
    // println!("{}", &answer_01);
    let answer_02 = part_02(&input);
    println!("{}", &answer_02);
}


fn part_01(data: &str) -> isize {
    let mut sum: isize = 0;
    for line in data.lines() {
        let digits: Vec<char> = line.chars().filter(|c| c.is_digit(10)).collect();
        let num_string = format!("{}{}", digits.first().unwrap(), digits.last().unwrap());
        sum = sum + num_string.parse::<isize>().unwrap();
    }
    sum
}

struct DigitWord {
    word: String,
    digit: char,
}

fn find_first_digit(line: &str, digit_words: &Vec<DigitWord>) -> char {

    let line = line.to_string();

    for i in 0..line.len() {
        if line.chars().nth(i).unwrap().is_digit(10) {
            return line.chars().nth(i).unwrap();
        }
        for dw in digit_words {
            if line[0..i+1].contains(&dw.word) {
                return dw.digit
            }
        }
    }
    ' '
}

fn find_last_digit(line: &str, digit_words: &Vec<DigitWord>) -> char {

    let line = line.to_string();

    for i in (0..line.len()).rev() {
        if line.chars().nth(i).unwrap().is_digit(10) {
            return line.chars().nth(i).unwrap();
        }
        for dw in digit_words {
            if line[i-1..].contains(&dw.word) {
                return dw.digit
            }
        }
    }
    ' '
}

fn part_02(data: &str) -> isize {
    let mut sum: isize = 0;

    let mut replace_digit_words: Vec<DigitWord> = Vec::new();
    replace_digit_words.push( DigitWord { word: "one".to_string(), digit: '1' });
    replace_digit_words.push( DigitWord { word: "two".to_string(), digit: '2' });
    replace_digit_words.push( DigitWord { word: "three".to_string(), digit: '3' });
    replace_digit_words.push( DigitWord { word: "four".to_string(), digit: '4' });
    replace_digit_words.push( DigitWord { word: "five".to_string(), digit: '5' });
    replace_digit_words.push( DigitWord { word: "six".to_string(), digit: '6' });
    replace_digit_words.push( DigitWord { word: "seven".to_string(), digit: '7' });
    replace_digit_words.push( DigitWord { word: "eight".to_string(), digit: '8' });
    replace_digit_words.push( DigitWord { word: "nine".to_string(), digit: '9' });

    for line in data.lines() {
        let first_digit: char = find_first_digit(&line, &replace_digit_words);
        let last_digit: char = find_last_digit(&line, &replace_digit_words);
        let num_string = format!("{}{}", first_digit, last_digit); 
        sum = sum + num_string.parse::<isize>().unwrap();
    }
    sum
}
