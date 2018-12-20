using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace skynet
{
    class Init
    {
        public static void InitMain()
        {
            // Creates the source folder if it doesn't exists
            Directory.CreateDirectory("src");
            string[,] dataFiles = Utils.dataFiles;

            // Checks each of the important files
            for(int i = 0; i < (dataFiles.GetLength(0) - 1); i++)
            {
                if (!File.Exists(dataFiles[i, 0]) || IsBelowThreshold(dataFiles[i,0], 24))
                {
                    using (var client = new WebClient())
                    {
                        Console.WriteLine("Downloading data from " + dataFiles[i, 1]);
                        client.DownloadFile(dataFiles[i, 1], dataFiles[i, 0]);
                    }
                }
            }
            if (!File.Exists(dataFiles[2,0]))
            {
                using (var client = new WebClient())
                {
                    Console.WriteLine("Downloading data from " + dataFiles[2,1]);
                    client.DownloadFile(dataFiles[2,0], dataFiles[2,0]);
                }
            }
            ReadJSON();

            // Annoucing that initialization is complete
            Console.WriteLine("Initialization is complete, starting Skynet");
        }

        // Generates usable data from JSON files
        private static void ReadJSON()
        {
            Console.WriteLine("Reading game data");
            Utils.GameData = JArray.Parse(File.ReadAllText(@"src/gameData.json"));
            Console.WriteLine("Reading software data");
            Utils.SoftwareData = JArray.Parse(File.ReadAllText(@"src/softwareData.json"));
            Console.WriteLine("Reading user data");
            Utils.UserData = JArray.Parse(File.ReadAllText(@"src/gameData.json"));
        }

        // Checks file age, returns true if file is older than hours
        private static bool IsBelowThreshold(string filename, int hours)
        {
            var threshold = DateTime.Now.AddHours(-hours);
            return !(File.GetCreationTime(filename) <= threshold);
        }
    }
}
