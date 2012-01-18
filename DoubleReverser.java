import java.lang.IllegalArgumentException;

/**
 * This reverses the words in a sentence by first reversing all the characters
 * in the sentence, then reversing the characters in each word so the ending
 * string has the words in the reverse order from the first reversal, but the
 * words are still in the right direction because of the second set of reversals.
 */
public class DoubleReverser implements IWordReverser {
	/** 
	 * Return a new string which reverses a the portion of the input string
	 * between firstIndex and lastIndex.
	 */
	private String reverseSubString(String input, int firstIndex, int lastIndex) {
		// TODO: How much can I speed up the function by removing these checks? reverseWords 
		// guarantees both are true
		if (firstIndex < 0 || firstIndex >= input.length())
			throw new IllegalArgumentException("The first index is out of bounds");
		if (lastIndex < 0 || lastIndex >= input.length())
			throw new IllegalArgumentException("The last index is out of bounds");
		if (firstIndex > lastIndex)
			throw new IllegalArgumentException("The first index is later than the last index");
			
		char[] str = input.toCharArray();
		
		// Swap each character in the first half of the array with the corresponding one in
		// the back half of the array
		for (int i = 0; i <= (lastIndex-firstIndex)/2; i++) {
			char temp = str[firstIndex+i];
			str[firstIndex+i] = str[lastIndex-i];
			str[lastIndex-i] = temp;
		}
		return new String(str);
	}

	public String reverseWords(String sentence) {
		if (sentence.length() <= 1)
			return sentence;
		
		// Reverse the whole sentence so the words are in the right order
		String reversedSentence = reverseSubString(sentence, 0, sentence.length()-1);
		
		// Reverse each word within the sentence so they are the right direction
		int lastWordBoundary = 0;
		boolean wasWhitespace = Character.isWhitespace(reversedSentence.charAt(0));
		for (int i = 1; i < sentence.length(); i++) {
			if (Character.isWhitespace(reversedSentence.charAt(i)) != wasWhitespace) {
				reversedSentence = reverseSubString(reversedSentence, lastWordBoundary, i-1);
				lastWordBoundary = i;
				wasWhitespace = !wasWhitespace;
			}
		}
		reversedSentence = reverseSubString(reversedSentence, lastWordBoundary, reversedSentence.length()-1);
		
		return reversedSentence;
	}
	
	public static void main(String[] args) {
		(new ReverserTests(new DoubleReverser())).run();
	}
}