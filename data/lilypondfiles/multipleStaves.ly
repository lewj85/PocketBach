\version "2.16.0"  % necessary for upgrading to future LilyPond versions

\language "english"

instrumentOne = \relative c' {
  c4 d e f |
  R1 |
  d'4 c b a |
  b4 g2 f4 |
  e1 |
}

instrumentTwo = \relative g' {
  R1 |
  g4 a b c |
  d4 c b a |
  g4 f( e) d |
  e1 |
}

<<
  \new Staff \instrumentOne
  \new Staff \instrumentTwo
  \new Staff \partcombine \instrumentOne \instrumentTwo
>>


