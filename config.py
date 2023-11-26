# -*- coding: utf-8 -*-
# some files have broken successors
SUCCESSOR_FIXES = {
    9180: 9220, # FFAMod (1.0) -> FFAMod (1.02)
    19448: 21714, # Goku -> Goku 2.0
    21503: 25915, # Big Boss (2.0) -> Big Boss (v3)
    63223: 76493, # Clan Mod (v1.0) -> Clan Mod (v1.08)
    69308: 73386 # Recolor of Major Kusanagi -> Recolor of 'Major Kusanagi' (v2)
}
NO_SUCCESSOR = [
    4294, # JediMod++ (v3.0) - I have no idea what the successor of that is
    9220 # FFAMod (1.02) - doesn't appear to have a successor?
]

# IDs to omit per the author's request or similar
BLACKLIST = [
    # files by afiNity
    66973, 71666, 71893, 73127, 74141, 74579, 86817, 104039, 117522,
    # The Arena of Ankor per request of Cody Small
    69132,
    # SiLink's readmes contain his mail, which he doesn't want online; editing the readme during processing would be a PITA, so they're simply blacklisted.
    89294, 90878, 95303,
    # Luciel's files
    91030, 92067, 87693, 87884, 87918, 92110, 89229, 91063, 59308, 92080, 90922, 89548, 91030, 89308,
    # Miso had already tried to get this off Filefront before, without success
    121988,
    # Reported as broken by Asgarath83
    118389, 118456, 121331, 121874, 121470, 118354,
    # Raschu's files
    69340, 71917, 79150, 80978, 81229, 83649, 85731, 93072, 96799, 113987, 113991, 114103, 114105, 115829, 116572,
    # Marshall_T
    99865, 99866, 87447,
    # PhysicWater
    49105,
    # Eric Whittle
    114641,
    # Seifer Almasy model
    30192,
    # PyroTechnics
    37268, 46708,
    # Fybo
    105129, 42796, 45692,
]

# categories to rename
CATEGORY_RENAMES = {
    u"Jedi Knight 2: Jedi Outcast Downloads": u"Jedi Outcast",
    u"Jedi Knight 3: Jedi Academy Downloads": u"Jedi Academy"
}

OVERRIDES = {
    # Author asked to have mail removed from readme
    97164 : {
        "readme": u"<span style=\"font-size:10px;font-family:arial;\">*********************************** <br>\r\nJedi Knight: Jedi Academy <br>\r\n*********************************** <br>\r\nTITLE**: The Real Starkiller<br>\r\nAUTHOR**: Me, Dur: Nultma <br>\r\nWEBSITE: srynubsdonthaveone<br>\r\nSkype: x_izero_x<br>\r\n<br>\r\nFILE NAME: starkiller.pk3<br>\r\nDATE RELEASED: 16 of Jan 2008<br>\r\n<br>\r\nCREDITS**: Starkiller is some psyco android something that likes killing stars, he is fully<br>\r\nsick and hates TFU and all the Galen Marek's out there.<br>\r\n<br>\r\nThis is made by me, it's ment to be crappy if your wondering XD<br>\r\n<br>\r\n<br>\r\nNOTES: Have fun, the only bug is the model itself, since it's so bad!<br>\r\n<br>\r\nInstillation: Put it in base folder or any other mod you have, whatever.<br>\r\n<br>\r\n<br>\r\nTHIS MODIFICATION IS NOT MADE, DISTRIBUTED, OR SUPPORTED BY ACTIVISION, RAVEN, OR <br>\r\nLUCASARTS ENTERTAINMENT COMPANY LLC. ELEMENTS TM &amp;  LUCASARTS <br>\r\nENTERTAINMENT COMPANY LLC AND/OR ITS LICENSORS.</span>",
    },
    76205: {
        "readme": u"<span style=\"font-size:10px;font-family:arial;\">******************************************<br>\r\nJEDI KNIGHT III : JEDI ACADEMY MODIFICATION<br>\r\n******************************************<br>\r\n<br>\r\n<br>\r\nTitle : HM Corran Horn<br>\r\nAuthor : Hessmix<br>\r\nFile Type: Re-skin<br>\r\nFile Name : HM_CorranHorn.pk3<br>\r\nFile Size : 6.73MB<br>\r\nOriginal Model: Hapslash's Anakin Skywalker Episode 2<br>\r\nModel's Creator: Hapslash<br>\r\nOriginal Textures Provided by: Hapslash<br>\r\nNew Textures Provided by: Hessmix<br>\r\n<br>\r\n<br>\r\n<br>\r\n------------------------------------------<br>\r\n------------------------------------------<br>\r\n<br>\r\nFirst off I would like to thank everyone from 'The Void' and their help in the making of this skin. (http://z9.invisionfree.com/Hapslashs_Void/)<br>\r\n<br>\r\nI would also like to thank Hapslash for a awesome model to work with, although I must say that Episode 3 Anakin is much easier to edit then Episode 2, though I do relish the challenge.<br>\r\n<br>\r\nAlso thank you to Buffy from the Void for awesome screenshots.<br>\r\n<br>\r\nOk now that I've done the thanking let me go on to describe what I've made here. This re-skin is my attempt to make Corran Horn, the other Jedi that came from Rogue Squadron. Recently a modification came out for Battlefront 2, which had a huge number of new choices for the game. One such choice was Corran Horn but to my surprise the Corran Horn had short hair. I liked the idea of him with short hair so I came up with this.<br>\r\n<br>\r\nI guess if I were to fit this in to the Expanded Universe this is after I, Jedi. Corran is still newly out of the Starfighter Corps (hence the short hair) but has revealed himself as Corran Horn to the Jedi. <br>\r\n<br>\r\n<br>\r\n<br>\r\nWhat does it look like?<br>\r\n<br>\r\nI basically took the Episode 2 Anakin and turned the robes a green-yellow hue. The Tabards are a light green (Default Model) and a Dark Green (DarkGreen Model) The boots are just straight black with an three straps instead of the regular two.<br>\r\n<br>\r\n<br>\r\nAdditional Information:<br>\r\n<br>\r\nI've added icons for the skins but just incase they don't work enter these codes on the console:<br>\r\n<br>\r\n/model hm_corranhorn<br>\r\n/model hm_corranhorn/darkgreen<br>\r\n/model hm_corranhorn/hood<br>\r\n/model hm_corranhorn/robe<br>\r\n<br>\r\n<br>\r\nInstallation:<br>\r\n<br>\r\nSimply extract the pk3 to the gamedata/base folder of your Jedi Academy directory. To uninstall simply remove or delete the file.</span>",
    },
    73888: {
         "readme": "<span style=\"font-size:10px;font-family:arial;\">Basically a vstr cfg which in MAKERMOD (and makermod only) it gives you some pretty good spy abilities. To use it in game, type in /exec spyscript3.cfg then press HOME to get a lowdown on the commands. Hope you enjoy :D<br>\r\n<br>\r\nTo install, extract the config file to your gamedata/base folder.<br>\r\n<br>\r\nBy reading this readme, at anytime, you have just accepted this as a contract, not hold the creator, website admin(s),<br>\r\nhosting the model, LucasArts, Raven, or any of the third parties mentioned in this document, responsible for any lawsuits<br>\r\nor legal issues that may or maynot incur.<br>\r\n-----------<br>\r\nCredits<br>\r\n__<br>\r\nToast: Without Toast, i wouldn't have JKA :) or have Makermod. He is the modding GOD!<br>\r\nScooper: For helping me out ALOT with scripting and giving me permission to use his 'menu' . Most credit to him!<br>\r\nUnsungHero: For inspiring me to script with his ninja scripts!.<br>\r\nLiberiFatili37: For support :D<br>\r\n-----------<br>\r\n<br>\r\n========================================================<br>\r\n\u00a9 2006 YOU MAY NOT COPY OR REDISTRIBUTE THIS ANYWHERE OTHERWISE MICHAEL JACKSON WILL COME FOR YOU! RAVENSOFT / LUCASARTS DID NOT DEVELOPE THIS MOD/SCRIPT THEREFORE IT IS NOT THEIRS! EVEN IF THEY CLAIM IT TO BE! MUHAAAAAAAAAAAAAHAHAHAHAHAHAHA *stab*stab*stab* I'm done :P</span>",
    },
}
