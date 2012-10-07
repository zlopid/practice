#include <iostream>
#include <stack>
#include <string>

/*
 Given a string with an expression that uses several types of brackets, like (),
 {}, and [], determine whether the brackets are valid, with end brackets matching
 beginning ones
*/

bool isStartBracket(char c) {
	return (c == '(') || (c == '{') || (c == '[');
}

bool isEndBracket(char c) {
	return (c == ')') || (c == '}') || (c == ']');
}

bool startEndBracketsMatch(char start, char end) {
	switch (end) {
	case ')':
		return (start == '(');
	case '}':
		return (start == '{');
	case ']':
		return (start == '[');
	default:
		return false;
	}
}

bool bracketsMatch(const std::string& input) {
	std::stack<char> brackets;
	for (int i = 0; i < input.size(); i++) {
		char current = input[i];
		if (isStartBracket(current)) {
			brackets.push(current);
		} else if (isEndBracket(current)) {
			if (brackets.empty() || !startEndBracketsMatch(brackets.top(), current))
				return false;
			brackets.pop();
		}
	}
	return brackets.empty();
}

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