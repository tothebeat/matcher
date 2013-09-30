matcher
=======

Written in Python using the [Django](https://docs.djangoproject.com/en/1.5/) web framework to make this accessible to people who don't want to use command lines (like me) to make use of a program. Using the [xlrd](https://pypi.python.org/pypi/xlrd/0.9.2) python library for reading XLSX spreadsheet files. I have no idea how xlrd works, it could be a tiny version of Excel for all I know. 

I have no idea what I'm doing. How did I get here.

The point of this project is to help solve the problem of matching data between files of different formats that do not share a common field. For example, let's say you have a file with home addresses for your friends:

<table>
  <tr>
    <th>row</th>
    <th>name</th>
    <th>address</th>
    <th>friends since</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Sally Albright</td>
    <td>New York, NY</td>
    <td>1977</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Sherlock Holmes</td>
    <td>221B Baker Street</td>
    <td>1881</td>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
  </tr>
  <tr>
    <td>2370</td>
    <td>Johnny Cash</td>
      <td>Nashville, TN</td>
    <td>2003</td>
  </tr>
</table>

You have a separate file with your friends' birthdays, but the names don't quite match:

<table>
  <tr>
    <th>row</th>
    <th>name</th>
    <th>birthday</th>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
  </tr>
  <tr>
    <td>16</td>
    <td>SALLY ALBRIGHT</td>
    <td>June 14</td>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
  </tr>
  <tr>
    <td>37</td>
    <td>j. cash</td>
    <td>February 26</td>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
  </tr>
  <tr>
    <td>14001</td>
    <td>Sherlock Holmes, Esq.</td>
    <td>January 6</td>
  </tr>  
</table>

Note the implied number of rows in this example. Matcher is meant to work with data that is just beyond the level of being manageable by hand. Sure, you could figure this out by hand, but do you really want to do it? 

I am writing this as a tool to formalize a lot of things I might do by hand when matching data. Hopefully I can also make this useful for someone else. 

