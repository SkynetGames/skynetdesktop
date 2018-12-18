using Avalonia;
using Avalonia.Markup.Xaml;

namespace skynet
{
    public class App : Application
    {
        public override void Initialize()
        {
            AvaloniaXamlLoader.Load(this);
        }
    }
}
