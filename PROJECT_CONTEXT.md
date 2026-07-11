\# BetLab Project Context



\## Project Name

BetLab - Football Betting Analysis System



\## Purpose

BetLab is a Python + Excel based football analysis system.



Main goals:

\- Collect worldwide football match data.

\- Analyze team and competition statistics.

\- Compare historical performance.

\- Create prediction and betting analysis models.

\- Export results to Excel.



\## Technology Stack



\- Python

\- Excel VBA (.xlsm)

\- Git / GitHub

\- JSON data storage



\## Repository



GitHub:

https://github.com/ME-BetLab/BetLab.git



Branch:

main



\## Current Folder Structure



BetLab/



\- config/

\- data/

&#x20; - raw/

&#x20; - processed/

\- docs/

\- excel/

&#x20; - BetLab\_v1.00.xlsm

\- logs/

\- scripts/

&#x20; - downloader.py

&#x20; - parser.py

&#x20; - matches.py

&#x20; - download\_test.py

&#x20; - \_\_init\_\_.py

\- tests/

\- betlab.py

\- .gitignore



\## Current Development Status



Completed:



✅ Git repository created  

✅ GitHub connection completed  

✅ Initial commit completed  

✅ Folder names normalized to lowercase  

✅ Python execution tested  

✅ Data downloader working  

✅ Parser working  

✅ Competition data retrieved  

✅ Premier League test data downloaded  



Current test:



League Count: 80



Successful data output:



data/raw/matches\_2\_44.json



\## Current Data Flow



Downloader

&#x20;   |

&#x20;   v

Raw JSON Data

&#x20;   |

&#x20;   v

Parser

&#x20;   |

&#x20;   v

Statistics Modules

&#x20;   |

&#x20;   v

Excel Reporting



\## Development Rules



\- Keep raw data separated from processed data.

\- Do not change architecture without checking existing modules.

\- Keep Git history clean.

\- Add new features step by step.

\- Maintain Excel compatibility.



\## Next Development Steps



1\. Analyze matches\_2\_44.json structure.

2\. Create standard match data model.

3\. Remove duplicate competitions.

4\. Create team statistics module.

5\. Export Python results to Excel.

6\. Build prediction model.



\## AI Assistant Notes



This is an ongoing software project.



When continuing:

\- Check existing files before suggesting new ones.

\- Preserve current architecture.

\- Remember Python + Excel integration is the final goal.

\- Treat BetLab as a real software project.

