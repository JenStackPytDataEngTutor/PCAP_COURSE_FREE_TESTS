phrases = ['when in rome', 
    'what goes around comes around', 
    'all is fair in love and war'
    ]
phrases.sort(key=lambda x: x.split()[0][1], reverse=True)
print(phrases)
