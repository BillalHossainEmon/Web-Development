//Literal Characters Regular Expression
let re = /hello/; //case sensitive
re = /hello/i; //case insensitive

str = 'Hello World!';

//Meta Characters Regular Expression
re = /^hello/; //^ means must start with
re = /hello$/; //$ means must end with
re = /world$/;
re = /^hello$/; //^ at the start and $ at the bottom means it must start and end with
re = /h.llo/; //. means it can be any character in that particular position
re = /h*llo/; //* means it can be any character 0 or more than once in that particular position
re = /he?llo/; //? means that character is option it's existance doesn't matter
re = /hello\?/; //\ means it will count the character as a string this is also called escaping

str = "Again hello World";
str = "hello hello";
str = "hello";
str = "hallo";
str = "hillo";
str = "h llo";
str = "hllo";
str = "hillo worlde";
str = "hello worlde";
str = "hillo";
str = "hilo";
str = "hhfsdhfsuillo";
str = "hello";
str = "hllo";
str = "hallo";
str = "htllo";
str = "heallo";
str = "hello";
str = "hallo";
str = "hllo";
str = "hello";
str = "hello?";

// Character Set using Brackets []
re = /h[eai]llo/; // Must any of them from the brackets
re = /[HA]ello/i; // Either H or A must be in the starting
re = /[^ha]ello/; // Anything except those from the brackets
re = /^[ha]ello/; // Must start with h or a
re = /[a-f]ello/; // setting range means it should be any character from a to f
re = /[A-Z]ello/; // Start with upper Case in other word case sensitive
re = /[A-Z]ello/i; // Case insensitive
re = /^[A-Z]/; // First Letter must be upper case
re = /^[a-z]/; // First Letter must be lower case
re = /[A-Za-z]ello/; // First letter has to be alphabet doesnt matter upper or lower case
re = /[0-9]ello/; //First Character must be a number
re = /^[0-9]ello/; //First Character must be a number and it must occur first in the string
re = /[^0-9]ello/; // Not digit should be there
re = /^[0-9][0-9][0-9]ello/; // three digits
re = /^[0-9][0-9][0-9][0-9][0-9]/ // 5 digits

// Braces {} - Quantifier
re = /el{2}o/; // Must occur exactly 2 times
re = /el{3}o/;
re = /hel{2,5}o/; // Range
re = /hel{2,}o/; // At least 2 times

// Parentheses () - Grouping
re = /^([0-9]){5}/; // /^[0-9][0-9][0-9][0-9][0-9]/ // 5 digits
re = /^([0-9]xy){4}/;

// Bangladeshi Phone Number
// total 11 digits
re = /^01[0-9]{9}$/;
//re = /^+8801[0-9]{9}$/;

str = "2xy3xy7xy8xy";
str = "01788888888";
str = "+8801811888889";

// Shorthand Character Classes
re = /w/; // Word Character - alpha numeric or _
re = /w+/; // One or more
re = /W/; // Non Word Character
re = /W+/; // one or more
re = /d/; // Digit
re = /d+/; // one or more digit
re = /D/; // Non digit
re = /s/; // Match white space
re = /S/; // Match non white space
re = /Hello\b/; // Word Boundary means there has to be a space after the word
re = /\bHello\b/; // Means there has to be a space before and after the word

// Assertions
re = /x(?=yz)/; // Matches x only if x is before y
re = /x(?!yz)/;


str = "fsdfxyzfdsf";


console.log(re.exec(str));

reTest(re, str);

function reTest(re, str) {
    if (re.test(str)) {
        console.log(`'${str}' matches '${re.source}`);
    } else {
        console.log(`'${str}' doesn't match`);
    }
}