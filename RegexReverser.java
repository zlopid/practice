import java.util.regex.*;
import java.util.LinkedList;

/**
 * Implements a word reversing algorithm using regular expressions.
 *
 * My first thought for a simple string parsing problem like this is to use a
 * regular expression. Here, I want to split the input into its words and 
 * whitespace components and then reverse them, which seems like a good fit for
 * a regex.
 *
 * The Java RegEx classes don't allow random or reverse access to the matches,
 * so I stored them in a stack implemented with a LinkedList. The LinkedList is
 * good because the algorithm inserts and removes from the front a lot, and it is
 * O(1) for that.
 *
 * Because a stack is FILO, when we pop the parts of the sentence, they come
 * back in reverse order.
 */
public class RegexReverser implements IWordReverser {
	public String reverseWords(String sentence) {
		Pattern wordOrWhitespace = Pattern.compile("[^\\s]+|\\s+");
		Matcher words = wordOrWhitespace.matcher(sentence);
		
		// Store all the matches in a stack
		LinkedList<String> splitWords = new LinkedList<String>();
		while(words.find())
			splitWords.push(words.group());	

		// Pop from the stack to aggregate the string in reversed-word order
		StringBuffer reversedSentence = new StringBuffer();
		while(splitWords.size() > 0)
			reversedSentence.append(splitWords.pop());

		return reversedSentence.toString();
	}
	
	public static void main(String[] args) {
		(new ReverserTests(new RegexReverser())).run();
	}
}
