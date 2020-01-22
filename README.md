## What's this
`partial_transform` command allows you to apply text transformation command to a part of each line.

## For example
### `partial_transform 2 'rev'`

You can reverse string just only on 2nd column in tsv file as below.

```bash
cat sample.tsv
policyID	statecode	county	eq_site_limit	hu_site_limit
119736	FL	CLAY COUNTY	498960	498960
448094	FL	CLAY COUNTY	1322376.3	1322376.3
206893	FL	CLAY COUNTY	190724.4	190724.4
333743	FL	CLAY COUNTY	0	79520.76
172534	FL	CLAY COUNTY	0	254281.5
785275	FL	CLAY COUNTY	0	515035.62

cat sample.tsv | partial_transform 2 'rev'
policyID	edocetats	county	eq_site_limit	hu_site_limit
119736	LF	CLAY COUNTY	498960	498960
448094	LF	CLAY COUNTY	1322376.3	1322376.3
206893	LF	CLAY COUNTY	190724.4	190724.4
333743	LF	CLAY COUNTY	0	79520.76
172534	LF	CLAY COUNTY	0	254281.5
785275	LF	CLAY COUNTY	0	515035.62
```

### `partial_transform 2 'rev | tr "A-Z" "a-z"'`
Of course, you can use pipe(`|`) as well as command-line.

```
cat sample.tsv | partial_transform 2 'rev | tr "A-Z" "a-z"'
policyID	edocetats	county	eq_site_limit	hu_site_limit
119736	lf	CLAY COUNTY	498960	498960
448094	lf	CLAY COUNTY	1322376.3	1322376.3
206893	lf	CLAY COUNTY	190724.4	190724.4
333743	lf	CLAY COUNTY	0	79520.76
172534	lf	CLAY COUNTY	0	254281.5
785275	lf	CLAY COUNTY	0	515035.62
```

## Install
You can install with pip.

```
pip install git+https://github.com/cm-hirano-shigetoshi/partial_transform
```

## Usage
```
usage: partial_transform [-F DELIMITER] nth command
```

`-F`: Specify delimiter. The default is awk style(separated with spaces and tabs).

