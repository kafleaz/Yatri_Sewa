using System;
namespace lab
{
    internal class Generic_Class
    {
        class Box<T>
        {
            private T contents; public Box(T item)
            {
                contents = item;
            }
            public T GetContents()
            {
                return contents;
            }
        }
        class MathHelper
        {
            public static T Max<T>(T a, T b) where T : IComparable<T>
            {
                return a.CompareTo(b) > 0 ? a : b;
            }
        }

        class Program
        {
            static void Main(string[] args)
            {
                Box<int> intBox = new 
                    Box<int>(42); int intContents = intBox.GetContents();
                Console.WriteLine($"Integer Contents: {intContents}");

                Box<string> stringBox = new 
                    Box<string>("Hello, Generics!"); 
                string stringContents = stringBox.GetContents();
                Console.WriteLine($"String Contents: {stringContents}");

                int maxInt = MathHelper.Max(10, 20); 
                Console.WriteLine($"Max Integer: {maxInt}");

                double maxDouble = MathHelper.Max(3.14, 2.71); 
                Console.WriteLine($"Max Double: {maxDouble}");
            }
        }
    }
}
