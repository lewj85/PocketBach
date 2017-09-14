\version "2.16.0"

% PocketBach Score by Jesse Lew
\language "english"

\parallelMusic #'(voiceA voiceB voiceC)
{
\relative c'' g1 | %1
\relative f' e1 | %1
\relative c c1 | %1

\relative c'' e1 | %2
\relative f' c1 | %2
\relative c a1 | %2

\relative c'' d1 | %3
\relative f' f1 | %3
\relative c d1 | %3

\relative c'' d1 | %4
\relative f' b1 | %4
\relative c g1 | %4

\relative c'' c1 | %5
\relative f' e1 | %5
\relative c c1 | %5

\relative c'' e1 | %6
\relative f' c1 | %6
\relative c a1 | %6

\relative c'' a1 | %7
\relative f' f1 | %7
\relative c f1 | %7

\relative c'' g1 | %8
\relative f' b1 | %8
\relative c g1 | %8

\relative c'' g1 | %9
\relative f' e1 | %9
\relative c c1 | %9

\relative c'' c1 | %10
\relative f' a1 | %10
\relative c a1 | %10

\relative c'' f1 | %11
\relative f' a1 | %11
\relative c d1 | %11

\relative c'' d1 | %12
\relative f' b1 | %12
\relative c g1 | %12

\relative c'' g1 | %13
\relative f' e1 | %13
\relative c e1 | %13

\relative c'' d1 | %14
\relative f' d1 | %14
\relative c f1 | %14

\relative c'' g1 | %15
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