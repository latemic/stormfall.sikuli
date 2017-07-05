import time
import array

Settings.LogTime = True

running = True
shouldTeachDragon = False
artifcatsToSell = ["1495845112956.png", "1495845279675.png", "1495845348616.png", Pattern("1496619723416.png").similar(0.90), Pattern("1496619844491.png").similar(0.90)]

#Region.setAutoWaitTimeout(3)
setFindFailedResponse(SKIP)

def runHotkey(event):
    global running
    running = False

def closeMessageBoxes():
    try:
        closeButtons = findAll("1496662347433.png")       
        if closeButtons is not None:
            for x in sorted(closeButtons, key = lambda m:m.y, reverse = True):
                Debug.log(1, 'Close button at %d:%d', x.x, x.y)
                click(x)
    except FindFailed:
        Debug.log(1, 'No message boxes found')    

def closeMessageBox():
    click(Pattern("1495950088485.png").similar(0.80))
    waitVanish(Pattern("1495950088485.png").similar(0.80))

def clickOrIgnore(pattern):
    try:
        click(pattern)
    except FindFailed:
        Debug.log(1, 'Pattern not found')

Env.addHotkey(Key.F1, KeyModifier.SHIFT, runHotkey)

# exists(Pattern("1495837589459.png").similar(0.90)) and
if exists(Pattern("1496662582187.png").similar(0.90)):
    click(Pattern("1496662582187.png").similar(0.90));

Debug.log(1, 'Entering main loop')

while (running):    
    closeMessageBoxes()
    
    #  Dragon ************************************
    if exists(Pattern("1495977053398.png").similar(0.90)):
        Debug.log(1, 'Open dragon options')
        clickOrIgnore(Pattern("1495977053398.png").similar(0.90))

        if exists(Pattern("1495921176461.png").similar(0.90)):
            click("1495921238338.png");
        
        #if exists(Pattern("1495921762111.png").similar(0.90)):
        clickOrIgnore("1495977251471.png");        
        
        while (exists("1495925875302.png") and running):
            clickOrIgnore(Pattern("1495925875302.png").targetOffset(81,-256));
            if exists(Pattern("1495925222870.png").similar(0.90)):
                clickOrIgnore(Pattern("1495925248280.png").similar(0.90));

        if exists(Pattern("1495925998593.png").similar(0.90).targetOffset(-41,11)):
            clickOrIgnore(Pattern("1495925998593.png").similar(0.90).targetOffset(-41,11));
            shouldTeachDragon = True
            mouseMove(0, 53);

        while (exists(Pattern("1495925998593.png").similar(0.90)) and shouldTeachDragon and running):
            #skillIcon = "1495927968714.png";
            skillIcon = Pattern("1496661884435.png").similar(0.90);
            #actionButtonIcon = Pattern("1495928189897.png").similar(0.90);
            actionButtonIcon = "1496661614120.png";
            if exists(skillIcon):
                clickOrIgnore(skillIcon);
                if exists(actionButtonIcon):
                    clickOrIgnore(actionButtonIcon);
                    closeMessageBox()
                else:
                    closeMessageBox()
                    shouldTeachDragon = False;

            mouseMove(0, 321);
            mouseDown(Button.LEFT);
            mouseMove(0, -321);
            mouseUp(Button.LEFT);

    # Mara ************************************    

    if exists(Pattern("1495977592064.png").similar(0.90)):
        clickOrIgnore(Pattern("1495977592064.png").similar(0.90))
        wait("1495977703811.png")
        clickOrIgnore(Pattern("1495977800193.png").similar(0.90).targetOffset(63,18))
        closeMessageBox()

    if exists(Pattern("1495977899878.png").similar(0.90)):
        clickOrIgnore(Pattern("1495977899878.png").similar(0.90))        
        while not exists("1495978835728.png") and running:
            clickOrIgnore("1495978878504.png")
            
        hover("1495978835728.png")
        mouseMove(-160, 0);
        
        while running:
            
            if exists("1495978957274.png"):
                clickOrIgnore("1495978957274.png")
                wait("1495979545073.png")
                clickOrIgnore("1495979545073.png")
                break
            
            mouseMove(0, 321);
            mouseDown(Button.LEFT);
            mouseMove(0, -321);
            mouseUp(Button.LEFT);        

        closeMessageBox()
    
           
                
            
#       if exists(Pattern("1495838297568.png").similar(0.90).targetOffset(-48,15)):
#           click(Pattern("1495838297568.png").similar(0.90).targetOffset(-48,15));

#            if exists(Pattern("1495839439508.png").similar(0.90).targetOffset(-2,144)):
 #               click(Pattern("1495839439508.png").similar(0.90).targetOffset(-2,144));
                
 #           while (exists(Pattern("1495839616610.png").similar(0.90)) and not exists(Pattern("1495840073273.png").similar(0.90)) 
 #                   and running):
 #               click(Pattern("1495839616610.png").similar(0.90).targetOffset(300,300));

    # Artifacts ************************************ 

        
    if exists(Pattern("1495844498166.png").similar(0.93)):
        clickOrIgnore(Pattern("1495844498166.png").similar(0.93).targetOffset(-15,-20));
        
        wait(Pattern("1496620744641.png").similar(0.90).targetOffset(-42,35))
        clickOrIgnore(Pattern("1496620744641.png").similar(0.90).targetOffset(-42,35))
        
        wait(Pattern("1496621224401.png").similar(0.90))
        clickOrIgnore(Pattern("1495844758443.png").similar(0.90))

        for art in artifcatsToSell:
            if exists(art):
                clickOrIgnore(art);
                clickOrIgnore("1495845241022.png");
                clickOrIgnore("1495845459491.png");
                break;
            
#        else: if exists("1495845279675.png"):
#            click("1495845279675.png");
#            click("1495845241022.png");
#            click("1495845459491.png");
#        else if exists("1495845348616.png"):
#            click("1495845348616.png");
#            click("1495845241022.png");
#            click("1495845459491.png");        
#        else if exists(Pattern("1496619723416.png").similar(0.90))
#            click(Pattern("1496619723416.png").similar(0.90));
#            click("1495845241022.png");
#            click("1495845459491.png");
#        else if exists(Pattern("1496619844491.png").similar(0.90))
#            click(Pattern("1496619844491.png").similar(0.90));
#            click("1495845241022.png");
#            click("1495845459491.png");           
    
    time.sleep(3)     