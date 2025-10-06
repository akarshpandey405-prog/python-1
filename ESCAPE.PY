| Escape Sequence | Meaning                   | Example                                    | Output                               |
| --------------- | ------------------------- | ------------------------------------------ | ------------------------------------ |
| `\\n`           | New line                  | `print("Hello\\nWorld")`                   | Hello<br>World                       |
| `\\t`           | Tab (horizontal)          | `print("Hello\\tWorld")`                   | Hello    World                       |
| `\\\\`          | Backslash (`\`)           | `print("This is a backslash: \\\\")`       | This is a backslash: \               |
| `\\'`           | Single quote              | `print('It\\'s fine')`                     | It's fine                            |
| `\\"`           | Double quote              | `print("He said \\"Hi\\"")`                | He said "Hi"                         |
| `\\r`           | Carriage return           | `print("Hello\\rWorld")`                   | World                                |
| `\\b`           | Backspace                 | `print("Helloo\\b")`                       | Hello                                |
| `\\f`           | Form feed (page break)    | `print("Hello\\fWorld")`                   | HelloWorld                          |
| `\\v`           | Vertical tab              | `print("Hello\\vWorld")`                   | HelloWorld                          |
| `\\a`           | Bell (alert sound)        | `print("\\a")`                             | (Makes a beep sound on some systems) |
| `\\N{name}`     | Unicode character by name | `print("\\N{GREEK CAPITAL LETTER DELTA}")` | Δ                                    |
| `\\uXXXX`       | Unicode (16-bit hex)      | `print("\\u03A9")`                         | Ω                                    |
| `\\UXXXXXXXX`   | Unicode (32-bit hex)      | `print("\\U0001F600")`                     | 😀                                   |
| `\\xXX`         | Character with hex value  | `print("\\x41")`                           | A                                    |
