\version "2.16.0"

% PocketBach Score by Jesse Lew
\language "english"

\parallelMusic #'(voiceA voiceB voiceC)
{
\relative c'' e1 | %1
\relative f' c1 | %1
\relative c c1 | %1

\relative c'' f1 | %2
\relative f' a1 | %2
\relative c d1 | %2

\relative c'' c1 | %3
\relative f' a1 | %3
\relative c e1 | %3

\relative c'' a1 | %4
\relative f' c1 | %4
\relative c f1 | %4

\relative c'' b1 | %5
\relative f' d1 | %5
\relative c g1 | %5

\relative c'' c1 | %6
\relative f' e1 | %6
\relative c a1 | %6

\relative c'' c1 | %7
\relative f' a1 | %7
\relative c f1 | %7

\relative c'' d1 | %8
\relative f' b1 | %8
\relative c g1 | %8

\relative c'' g1 | %9
\relative f' e1 | %9
\relative c c1 | %9

\relative c'' a1 | %10
\relative f' f1 | %10
\relative c d1 | %10

\relative c'' e1 | %11
\relative f' a1 | %11
\relative c c1 | %11

\relative c'' f1 | %12
\relative f' a1 | %12
\relative c f1 | %12

\relative c'' g1 | %13
\relative f' e1 | %13
\relative c c1 | %13

\relative c'' e1 | %14
\relative f' c1 | %14
\relative c g1 | %14

\relative c'' d1 | %15
\relative f' b1 | %15
\relative c g1 | %15

\relative c'' c1 | %16
\relative f' e1 | %16
\relative c c1 | %16

}
\new StaffGroup <<
  \new Staff << \relative c'' \voiceA \\ \relative c' \voiceB >>
  \new Staff \relative c { \clef bass \voiceC }
>>