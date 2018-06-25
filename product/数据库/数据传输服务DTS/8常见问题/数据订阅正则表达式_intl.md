## What is a regular expression?

> A regular expression is used to retrieve text that meets a certain pattern from text.

It matches a string from left to right. We generally use "regex" or "regexp" for short.
A regular expression can be used to replace text in strings, validate forms, and extract strings from a string based on pattern matching.
<br />

Imagine that you are writing an application, and you want to set rules for users to select usernames. We want usernames to contain letters, numbers, underscores, and hyphens.
To make it look good, we also want to limit the number of characters for a username. We can use the following regular expression to verify usernames:

<p align="center">
<img src="https://main.qcloudimg.com/raw/e8172d0afc4938e5f19d67ed6b9409c7.png" alt="Regular expression">
</p>

The above regular expression can match `john_doe`, `jo-hn\_doe`, and `john12\_as`. However, it cannot match `Jo` which contains an uppercase character and is too short.

## Contents

- [Basic Match](#.E5.9F.BA.E6.9C.AC.E5.8C.B9.E9.85.8D)
- [Metacharacter](#.E5.85.83.E5.AD.97.E7.AC.A6)
  - [Period](#.E8.8B.B1.E6.96.87.E5.8F.A5.E5.8F.B7)
  - [Character Set](#.E5.AD.97.E7.AC.A6.E9.9B.86)
     - [Negative Character Set](#.E5.90.A6.E5.AE.9A.E5.AD.97.E7.AC.A6.E9.9B.86)
  - [Repetition](#.E9.87.8D.E5.A4.8D)
     - [Asterisk](#.E6.98.9F.E5.8F.B7)
     - [Plus Sign](#.E5.8A.A0.E5.8F.B7)
     - [Question mark](#.E9.97.AE.E5.8F.B7)
  - [Curly Bracket](#.E8.8A.B1.E6.8B.AC.E5.8F.B7)
  - [Character Group](#.E5.AD.97.E7.AC.A6.E7.BB.84)
  - [Branch Structure](#.E5.88.86.E6.94.AF.E7.BB.93.E6.9E.84)
  - [Escape Special Character](#.E8.BD.AC.E4.B9.89.E7.89.B9.E6.AE.8A.E5.AD.97.E7.AC.A6)
  - [Locator](#.E5.AE.9A.E4.BD.8D.E7.AC.A6)
     - [Caret](#.E5.85.A5.E7.AC.A6.E5.8F.B7)
     - [Dollar Sign](#.E7.BE.8E.E5.85.83.E7.AC.A6.E5.8F.B7)
- [Abbreviated Character Set](#.E7.AE.80.E5.86.99.E5.AD.97.E7.AC.A6.E9.9B.86)
- [Assertion](#.E6.96.AD.E8.A8.80)
  - [Positive Lookahead Assertion](#.E6.AD.A3.E5.90.91.E5.85.88.E8.A1.8C.E6.96.AD.E8.A8.80)
  - [Negative Lookahead Assertion](#.E8.B4.9F.E5.90.91.E5.85.88.E8.A1.8C.E6.96.AD.E8.A8.80)
  - [Positive Lookbehind Assertion](#.E6.AD.A3.E5.90.91.E5.90.8E.E8.A1.8C.E6.96.AD.E8.A8.80)
  - [Negative Lookbehind Assertion](#.E8.B4.9F.E5.90.91.E5.90.8E.E8.A1.8C.E6.96.AD.E8.A8.80)
- [Label](#.E6.A0.87.E8.AE.B0)
  - [Case Insensitive](#.E4.B8.8D.E5.8C.BA.E5.88.86.E5.A4.A7.E5.B0.8F.E5.86.99)
  - [Global Search](#.E5.85.A8.E5.B1.80.E6.90.9C.E7.B4.A2)
  - [Multiline Match](#.E5.A4.9A.E8.A1.8C.E5.8C.B9.E9.85.8D)
- [Common Regular Expression](#.E5.B8.B8.E7.94.A8.E6.AD.A3.E5.88.99.E8.A1.A8.E8.BE.BE.E5.BC.8F)

## Basic Match

Regular expressions are patterns we use to retrieve letters and numbers in text. For example, the regular expression `cat` indicates: the letter `c` followed by letters `a` and `t`.

<pre>
"cat" => The <a href="#learn-regex"><strong>cat</strong></a> sat on the mat
</pre>

The regular expression `123` matches the string "123". Regular matching is done by comparing each character in the regular expression with that in the string to be matched one by one.
Regular expressions are generally case sensitive, so the regular expression `Cat` does not match the string "cat".

<pre>
"Cat" => The cat sat on the <a href="#learn-regex"><strong>Cat</strong></a>
</pre>

## Metacharacter

Metacharacters are the basic elements of regular expressions. Metacharacters here are not the same as usual, but are interpreted in a special way. Some metacharacters in square brackets have special meaning.
Here are the metacharacters:

| Metacharacter | Description |
|:----:|----|
| . | Match any characters other than line breaks. |
| [ ] | Character class. Match any characters enclosed in square brackets. |
| [^ ] | Negative character class. Match any characters not enclosed in square brackets.
| * | Match the preceding subexpression zero or more times |
| + | Match the preceding subexpression one or more times |
| ? | Match the previous subexpression zero or one time, or specify a non-greedy qualifier. |
| {n,m} | Curly bracket. Match the preceding character at least n times, but not more than m times. |
| (xyz) | Character group. Match the character xyz in an exact order. |
| &#124; | Branch structure. Match characters before or after the symbol. |
| &#92; | Escape character. It can restore the original meaning of metacharacters, allowing you to match reserved characters <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code> |
| ^ | Match the start of the line |
| $ | Match the end of the line |

### Period

The period `.` is the simplest example of a metacharacter. The metacharacter `.` can match any single character. It does not match a line break or a new line character. For example, the regular expression `.ar` indicates: any characters followed by letters `a` 
and `r`.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

### Character set

A character set is also called character class. Square brackets are used to specify the character set. Specify the character range using the hyphen within the character set. The order of the character ranges in square brackets can be ignored.
For example, the regular expression `[Tt]he` indicates: uppercase `T` or lowercase `t` followed by the letters `h` and `e`.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

However, the period in the character set indicates its literal meaning. The regular expression `ar[.]` indicates the lowercase letter `a` followed by the letter `r` and a period `.` character.

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

#### Negative character set

In general, the insertion character `^` indicates the start of a string. However, if it appears in square brackets, it cancels the character set. For example, the regular expression `[^c]ar` indicates: any characters other than the letter `c` followed by the character `a` and 
letter `r`.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

### Repetition

The following metacharacters `+`, `*` or `?` are used to specify how many times the sub-pattern can appear. These metacharacters work differently in different situations.

#### Asterisk

The symbol `*` indicates matching the previous matching rule zero or more times. The regular expression `a*` indicates that the lowercase `a` can be repeated zero or more times. But if it appears after a character set or character class, it indicates the repetition of the entire character set.
For example, the regular expression `[a-z]*` indicates: a line containing any number of lowercase letters.

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

The symbol `*` can be used with the meta symbol `.` to match any string `.*`. The symbol `*` can be used with the space character `\s` to match a string of space characters.
For example, the regular expression `\s*cat\s*` indicates: zero or more spaces followed by a lowercase letter `c`, a lowercase letter `a`, a lowercase letter `t`, and zero or more spaces.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

#### Plus sign

The symbol `+` matches the previous character one or more times. For example, the regular expression `c.+t` indicates: a lowercase letter `c` followed by any number of characters and a lowercase letter `t`.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

#### Question mark

In regular expressions, the metacharacter `?` is used to indicate that the previous character is optional. This symbol matches the previous character zero or one time.
For example, the regular expression `[T]?he` indicates: the optional uppercase letter `T` followed by a lowercase letter `h` and a lowercase letter `e`.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>
<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

### Curly bracket

Curly brackets (also called quantifier ?) are used in regular expressions to specify the number of times a character or a group of characters can be repeated. For example, the regular expression `[0-9]{2,3}` indicates: matching at least 2 numbers but no more than 3 numbers (characters ranging from 0 to 9).

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

We can omit the second number. For example, the regular expression `[0-9]{2,}` indicates: matching 2 or more numbers. If we delete the comma, the regular expression `[0-9]{2}` indicates: matching exactly two-digit numbers.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

<pre>
"[0-9]{2}" => The number was 9.<a href="#learn-regex"><strong>99</strong></a><a href="#learn-regex"><strong>97</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

### Character group

A character group is a set of sub-patterns written in parentheses `(...)`. As we discussed in regular expressions, if we put a quantifier after a character, the previous character is repeated.
However, if we put a quantifier after a character group, the entire character group is repeated.
For example, the regular expression `(ab)*` indicates matching zero or more strings "ab". We can also use the metacharacter `|` in a character group. For example, the regular expression `(c|g|p)ar` indicates: the lowercase letter `c`, `g` or `p` followed by letters `a` and `r`.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

### Branch structure

The vertical bar `|` is used to define the branch structure in a regular expression. The branch structure is like the condition between multiple expressions. Now you may think that this character set works in the same way as the branch structure.
But the difference is that the character set is only used at the character level, while the branch structure can be used at the expression level.
For example, the regular expression `(T|t)he|car` indicates: the uppercase letter `T` or lowercase letter `t` is followed by a lowercase letter `h`, a lowercase letter `e` or lowercase letter `c`, then a lowercase letter `a`, and a lowercase letter `r`.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

### Escape special character

Use the backslash `\` in the regular expression to escape the next character. This allows you to use reserved characters as the matching characters `{ } [ ] / \ + * . $ ^ | ?`. You can use it as a matching character by adding a `\` before a special character.
For example, the regular expression `.` is used to match any characters other than line breaks. To match the `.` character in the input string, the regular expression `(f|c|m)at\.?` indicates: the lowercase letter `f`, `c`, or `m` followed by a lowercase letter `a`, a lowercase letter `t`, and an optional `.` character.

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

### Locator

In regular expressions, we use locators to check whether the matching symbol is a start or end symbol.
There are two types of locators: `^`, which checks if the matching character is the start character, and `$`, which checks if the matching character is the end character of an input string.

#### Caret

The caret `^` is used to check if the matching character is the first character of an input string. If we use the regular expression `^a` (if "a" is the start symbol) to match the string `abc`, it matches `a`.
But if we use the regular expression `^b`, it matches nothing, because "b" in the string `abc` is not the start character.
Take a look at another regular expression `^(T|t)he`, which indicates: the uppercase letter `T` or lowercase letter `t` is the start symbol of the input string, followed by a lowercase letter `h` and a lowercase letter `e`.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

#### Dollar sign

Dollar sign `$` is used to check if the matching character is the last character of an input string. For example, the regular expression `(at\.)$` indicates: the lowercase letter `a` followed by the lowercase letter `t` and character `.`, and this matcher must be the end of the string.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

<pre>
"(at\.)$" => The fat cat sat on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

## Abbreviated Character Set

Regular expressions provide abbreviations for common character sets and regular expressions. The abbreviated character set is as follows:

| Abbreviation | Description |
|:----:|----|
| . | Match any characters other than line breaks |
| \w | Match all alphanumeric characters: `[a-zA-Z0-9_]` |
| \W | Match non-alphanumeric characters: `[^\w]` |
| \d | Match numeric characters: `[0-9]` |
| \D | Match non-numeric characters: `[^\d]` |
| \s | Match space characters: `[\t\n\f\r\p{Z}]` |
| \S | Match non-space characters: `[^\s]` |

## Assertion

Lookbehind assertions and lookahead assertions are sometimes referred to as assertions, which are special types of ***non-capturing groups*** (used for matching pattern, but not included in the matching list). When we use this pattern before or after a particular pattern, we use assertions first.
For example, we want to obtain all the numbers before the character `$` in the input string `$4.44 and $10.88`. We can use this regular expression `(?<=\$)[0-9\.]*` to indicate: get all numbers before the character `$` with the character `.` included.
The followings are the assertions used in regular expressions:

| Symbol | Description |
|:----:|----|
| ?= | Positive lookahead assertion |
| ?! | Negative lookahead assertion |
| ?<= | Positive lookbehind assertion |
| ?<! | Negative lookbehind assertion |

### Positive lookahead assertion

For positive lookahead assertions, the first part of the expression must be a lookahead assertion expression. The returned matching result only contains the text that matches the first part of the expression.
To define a positive lookahead assertion in brackets, the question mark and equal sign in brackets are expressed as `(?=...)`. The lookahead assertion expression is put after the equal sign in brackets.
For example, the regular expression `(T|t)he(?=\sfat)` indicates: matching uppercase letter `T` or lowercase letter `t`, which is followed by letters `h` and `e`.
In brackets, we define a positive lookahead assertion that leads the regular expression engine to match `The` or `the` which is followed by `fat`.

<pre>
"(T|t)he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

### Negative lookahead assertion

When we need to obtain the content mismatching the expression from an input string, we use a negative lookahead assertion. Negative lookahead assertion is defined in the same way as positive lookahead assertion.
The only difference is that we use negation symbol `!` instead of equal sign `=`, such as `(?!...)`.
Take a look at the following regular expression `(T|t)he(?!\sfat)`, which indicates: get all `The` or `the` mismatching `fat` from the input string, with a space character added before `fat`.

<pre>
"(T|t)he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

### Positive lookbehind assertion

Positive lookbehind assertions are used to obtain all matching content before a particular pattern. The positive lookbehind assertion is expressed as `(?<=...)`. For example, the regular expression `(?<=(T|t)he\s)(fat|mat)` indicates: get all the `fat` and `mat` behind the word `The` or `the` from the input string.

<pre>
"(?<=(T|t)he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>


### Negative lookbehind assertion

Negative lookbehind assertions are used to obtain all matching content that are not before a particular pattern. Negative lookbehind assertions are expressed as `(?<!...)`. For example, the regular expression `(?<!(T|t)he\s)(cat)` indicates: get all the `cat` that are not behind `The` or `the` in the input characters.

<pre>
"(?&lt;!(T|t)he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

## Label

Label modifies the output of the regular expression, which is also called modifier. The following labels can be used in any order or combination, and are part of a regular expression.

| Label | Description |
|:----:|----|
| i | Case insensitive: Set the matching rule as case insensitive. |
| g | Global search: Search the entire input string for all matching content. |
| m | Multiline match: Match each line of the input string. |

### Case insensitive

The modifier `i` is used to perform case-insensitive matching. For example, the regular expression `/The/gi` indicates: the uppercase letter `T` followed by a lowercase letter `h` and a letter `e`.
But at the end of regular matching, the label `i` informs the regular expression engine to ignore it. As you can see, we also use the label `g` because we want to search the entire input string for matching content.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

### Global search

The modifier `g` is used to perform a global match (it finds all matching items, and will not stop until the first one is found).
For example, the regular expression `/.(at)/g` indicates: any characters other than line breaks followed by a lowercase letter `a` and a lowercase letter `t`.
Because we use the label `g` at the end of the regular expression, it finds each matching item from the entire input string.

<pre>
".(at)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

### Multiline match

The modifier `m` is used to perform a multiline match. As we discussed earlier about `(^, $)`, use a locator to check whether the matching character is the start or the end of an input string. However, we want to use a locator for each line, so we use the modifier `m`.
For example, the regular expression `/at(.)?$/gm` indicates: the lowercase letter `a`, followed by the lowercase letter `t` matching any character other than line breaks zero or one time. And because of the label `m`, the regular expression engine matches the end of each line in the string.

<pre>
"/.at(.)?$/" => The fat
                cat sat
    
		on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

## Common Regular Expression
<table>
	<tbody>
		<tr>
			<td><center>
				<span style="font-size:14px;">Type</span><br>
			</td>
			
			<td><center>
				<span style="font-size:14px;">Expression</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">Positive integer</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^-\d+$</span><br>
			</td>
		</tr>
		
		<tr>
			<td><center>
				<span style="font-size:14px;">Negative integer</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^-\d+$</span><br>
			</td>
		</tr>
	
		<tr>
			<td><center>
				<span style="font-size:14px;">Phone number</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^+?[\d\s]{3,}$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">Phone code</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^+?[\d\s]+(?[\d\s]{10,}$</span><br>
			</td>
		</tr>
		
		<tr>
			<td><center>
				<span style="font-size:14px;">Integer</span><br>
		</td> 
		
			<td>
				<span style="font-size:14px;">^-?\d+$</span><br>
			</td>
		</tr>
		
		<tr>
			<td><center>
				<span style="font-size:14px;">User name</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^[\w\d_.]{4,16}$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">Alphanumeric characters</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^[a-zA-Z0-9]*$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">Alphanumeric characters with spaces</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^[a-zA-Z0-9 ]*$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">Password</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^(?=^.{6,}$)((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z]))^.*$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">Email</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})*$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">IPv4 address</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))*$`</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">Lowercase letter</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^([a-z])*$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">Uppercase letter</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^([A-Z])*$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">User name</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^[\w\d_.]{4,16}$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">Website</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^(((http|https|ftp):\/\/)?([[a-zA-Z0-9]\-\.])+(\.)([[a-zA-Z0-9]]){2,4}([[a-zA-Z0-9]\/+=%&_\.~?\-]*))*$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">VISA credit card number</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^(4[0-9]{12}(?:[0-9]{3})?)*$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">Date <br>(MM/DD/YYYY)</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2}$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">Date<br> (YYYY/MM/DD)</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^(19|20)?[0-9]{2}[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])$</span><br>
			</td>
		</tr>
	 
		<tr>
			<td><center>
				<span style="font-size:14px;">MasterCard credit card number</span><br>
			</td>
			
			<td>
				<span style="font-size:14px;">^(5[1-5][0-9]{14})*$</span><br>
			</td>
		</tr>
	
 	 </tbody>
</table>

