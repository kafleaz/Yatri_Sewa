using System;
namespace lab
{
    internal class ConvertString
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a string to convert to uppercase:");
            string inputUpper = Console.ReadLine();
            string upperCase = inputUpper.ToUpper();
            Console.WriteLine("Uppercase: " + upperCase);
            Console.WriteLine("Enter a string to convert to lowercase:");
            string inputLower = Console.ReadLine();
            string lowerCase = inputLower.ToLower();
            Console.WriteLine("Lowercase: " + lowerCase);
        }
    }
}
