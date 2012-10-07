#include <iostream>
#include <stack>
#include <string>

/*
 Given a string with an expression that uses several types of brackets, like (),
 {}, and [], determine whether the brackets are valid, with end brackets matching
 beginning ones
*/

// To make it easier to read the code, encapsulate these simple checks in functions
bool isStartBracket(char c) {
	return (c == '(') || (c == '{') || (c == '[');
}

bool isEndBracket(char c) {
	return (c == ')') || (c == '}') || (c == ']');
}

bool startEndBracketsMatch(char start, char end) {
	switch (end) {
	case ')': return (start == '(');
	case '}': return (start == '{');
	case ']': return (start == '[');
	default: return false;
	}
}

/**
 * Determine whether end brackets match the starting ones
 * by tracking the last start bracket in a stack.
 *
 * @param[in] input the expression to check
 * @return true if all start brackets have matching end brackets,
 *   and there are no extra end brackets.
 */
bool bracketsMatch(const std::string& input) {
	std::stack<char> startBrackets;
	for (int i = 0; i < input.size(); i++) {
		char current = input[i];
		
		if (isStartBracket(current)) {
			startBrackets.push(current);
			
		} else if (isEndBracket(current)) {
			if (startBrackets.empty() // end bracket before start bracket
				|| !startEndBracketsMatch(startBrackets.top(), current)) { // mismatch
				return false;
			}
			startBrackets.pop();
		}
	}
	return startBrackets.empty(); // extra start brackets
}

/**
 * Check that the result of bracketsMatch matches the expected output
 * and print a line in TAP format
 * @return the number of failed tests
 */
int test(const std::string& input, bool expected) {
	bool actual = bracketsMatch(input);
	if (actual != expected)
		std::cout << "not ";
	std::cout << "ok: " << input << std::endl;
	return (actual == expected) ? 0 : 1;
}

int main(int argc, char *argv[]) {
	int failingTests = 0;
	failingTests += test("", true);
	failingTests += test("()", true);
	failingTests += test("(", false);
	failingTests += test(")", false);
	failingTests += test(")(", false);
	failingTests += test("( { [ ] } )", true);
	failingTests += test("(}", false);
	failingTests += test("(})}", false);
	failingTests += test("{a: bc(d[3]-e[2])}", true);
	std::cout << "# " << failingTests << " tests failed" << std::endl;
}