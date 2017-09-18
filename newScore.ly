\version "2.16.0"

% PocketBach Score by Jesse Lew
\language "english"

\parallelMusic #'(voiceA voiceB voiceC)
{
\relative c'' r1 | %1
\relative f' | %1
\relative c | %1

\relative c'' | %2
\relative f' | %2
\relative c | %2

\relative c'' | %3
\relative f' | %3
\relative c | %3

\relative c'' | %4
\relative f' | %4
\relative c | %4

\relative c'' | %5
\relative f' | %5
\relative c | %5

\relative c'' | %6
\relative f' | %6
\relative c | %6

\relative c'' | %7
\relative f' | %7
\relative c | %7

\relative c'' | %8
\relative f' | %8
\relative c | %8

\relative c'' | %9
\relative f' | %9
\relative c | %9

\relative c'' | %10
\relative f' | %10
\relative c | %10

\relative c'' | %11
\relative f' | %11
\relative c | %11

\relative c'' | %12
\relative f' | %12
\relative c | %12

\relative c'' | %13
\relative f' | %13
\relative c | %13

\relative c'' | %14
\relative f' | %14
\relative c | %14

\relative c'' | %15
\relative f' | %15
\relative c | %15

\relative c'' | %16
\relative f' | %16
\relative c | %16

\relative c'' }
\new StaffGroup <<
  \new Staff << \relative c'' \voiceA \\ \relative c' \voiceB >>
  \new Staff \relative c { \clef bass \voiceC }
>>