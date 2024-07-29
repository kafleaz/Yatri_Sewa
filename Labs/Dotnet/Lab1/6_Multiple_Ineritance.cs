using System;
namespace lab
{
    internal class Multiple_Inheritance
    {
        interface IShape
        {
            double CalculateArea();
        }
        interface IColor
        {
            string GetColor();
        }

        class Circle : IShape, IColor
        {
            private double Radius { get; }
            private string Color { get; }

            public Circle(double radius, string color)
            {
                Radius = radius;
                Color = color;
            }
            public double CalculateArea()
            {
                return Math.PI * Math.Pow(Radius, 2);
            }
            public string GetColor()
            {
                return Color;
            }
        }

        class Program
        {
            static void Main(string[] args)
            {
                Circle redCircle = new Circle(5, "Red");

                double area = redCircle.CalculateArea(); 
                string color = redCircle.GetColor(); 
                Console.WriteLine($"Area of Circle: {area}");
                Console.WriteLine($"Area of Circle: {color}");
            }
        }
    }
}
