#include <iostream>
#include <stack>
#include <string>

/*
 Given a string with an expression that uses several types of brackets, like (),
 {}, and [], determine whether the brackets are valid, with end brackets matching
 beginning ones
*/
bool bracketsMatch(const std::string& input) {
	int brackets = 0;
	for (int i = 0; i < input.size(); i++) {
		switch(input[i]) {
		case '(':
			brackets++;
			break;
		case ')':
			brackets--;
			break;
		}
	}
	return brackets == 0;
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
	std::cout << "# " << failingTests << " tests failed" << std::endl;
}