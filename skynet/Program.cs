using Avalonia;
using Avalonia.Logging.Serilog;

namespace skynet
{
    class Program
    {
        static void Main(string[] args)
        {
            Init.InitMain();
            BuildAvaloniaApp().Start<MainWindow>();
        }


        public static AppBuilder BuildAvaloniaApp()
            => AppBuilder.Configure<App>()
                .UsePlatformDetect()
                .LogToDebug();
    }
}
