#include <iostream>
#include <stack>
#include <string>

bool bracketsMatch(const std::string& input) {
	return false;
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
	std::cout << "# " << failingTests << " tests failed" << std::endl;
}