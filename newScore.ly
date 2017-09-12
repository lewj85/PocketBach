\version "2.16.0"

% PocketBach Score by Jesse Lew
\language "english"

\parallelMusic #'(voiceA voiceB voiceC)
{
e1 |
\relative f' g1 |
\relative c c1 |

\relative c'' c1 |
\relative f' e1 |
\relative c a1 |

\relative c'' a1 |
\relative f' c1 |
\relative c f1 |

\relative c'' c1 |
\relative f' e1 |
\relative c c1 |

\relative c'' g1 |
\relative f' b1 |
\relative c g1 |

\relative c'' e1 |
\relative f' c1 |
\relative c a1 |

\relative c'' d1 |
\relative f' f1 |
\relative c d1 |

\relative c'' d1 |
\relative f' b1 |
\relative c g1 |

\relative c'' g1 |
\relative f' e1 |
\relative c c1 |

\relative c'' c1 |
\relative f' a1 |
\relative c a1 |

\relative c'' a1 |
\relative f' c1 |
\relative c f1 |

\relative c'' e1 |
\relative f' g1 |
\relative c c1 |

\relative c'' e1 |
\relative f' g1 |
\relative c c1 |

\relative c'' f1 |
\relative f' a1 |
\relative c f1 |

\relative c'' g1 |
\relative f' b1 |
\relative c g1 |

\relative c'' c1 |
\relative f' e1 |
\relative c c1 |

}
\new StaffGroup <<
  \new Staff << \relative c'' \voiceA \\ \relative c' \voiceB >>
  \new Staff \relative c { \clef bass \voiceC }
>>