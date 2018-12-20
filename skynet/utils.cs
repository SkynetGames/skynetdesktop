using System;
using System.Collections.Generic;
using Newtonsoft.Json.Linq;

namespace skynet
{
    class Utils
    {
        // Local and remote locations of all important JSON files
        public static string[,] dataFiles = new string[,]
        {
            { "src/gameData.json", "https://s3.amazonaws.com/skynet-metadata/game_data.json" },
            { "src/softwareData.json", "https://s3.amazonaws.com/skynet-metadata/software.json" },
            { "src/userData.json", "https://s3.amazonaws.com/skynet-desktop/usr_prefs.json" }
        };

        // Lists generated from the JSON files
        public static JArray GameData;
        public static JArray SoftwareData;
        public static JArray UserData;

        // The color pallet of Skynet, this is never used...
        public static string[] Colors = new string[]
        {
            "#b0bec5", // Light Blue
            "#546e7a", // Middle Blue
            "#263238"  // Dark Blue
        };
    }
}
