interface IWordReverser {
	/**
	 * Reverses the order of the words within a sentence.
	 * For instance: "Hello World!" becomes "World! Hello"
	 * 
	 * White space between the words should also be reversed,
	 * but the letters within the words should not be.
	 */
	public String ReverseWords(String sentence);
}