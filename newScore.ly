\version "2.16.0"

% PocketBach Score by Jesse Lew
\language "english"

\parallelMusic #'(voiceA voiceB voiceC)
{
e1 |
c1 |
c1 |

d1 |
d1 |
b1 |

c1 |
e1 |
c1 |

g1 |
c1 |
c1 |

c1 |
a1 |
f1 |

g1 |
c1 |
c1 |

f1 |
c1 |
f1 |

g1 |
d1 |
g1 |

g1 |
g1 |
c1 |

g1 |
g1 |
d1 |

c1 |
e1 |
c1 |

e1 |
e1 |
c1 |

c1 |
c1 |
c1 |

f1 |
f1 |
d1 |

d1 |
d1 |
g1 |

e1 |
g1 |
c1 |

}
\new StaffGroup <<
  \new Staff << \relative c'' \voiceA \\ \relative c' \voiceB >>
  \new Staff \relative c { \clef bass \voiceC }
>>