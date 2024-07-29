using System;
namespace lab
{
    internal class StringInterchange
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a string:"); 
            string input = Console.ReadLine(); 
            string result = SwapFirstAndLastCharacters(input);
            Console.WriteLine("Modified string: " + result);
        }

        static string SwapFirstAndLastCharacters(string input)
        {
            if (string.IsNullOrEmpty(input) || input.Length == 1) return input;

            char[] charArray = input.ToCharArray(); 
            char firstChar = charArray[0];
            char lastChar = charArray[input.Length - 1]; 
            charArray[0] = lastChar;
            charArray[input.Length - 1] = firstChar; 
            return new string(charArray);
        }
    }
}
