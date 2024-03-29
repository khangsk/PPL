// Generated from c:\Users\KHANG\Desktop\PPL\Tutorials\1. Lexical\Final\Final.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class Final extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		REAL=1, ID=2, STRING=3, WS=4;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LOWERCASE_LETTER", "DIGIT", "SIGN", "SCIENTIFIC", "DECIMAL_POINT", "EXP", 
			"REAL", "ID", "STRING", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "REAL", "ID", "STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public Final(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Final.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6u\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\3\2\3\2\3\3\3\3\3\4\5\4\35\n\4\3\5\3\5\3\5\6\5\"\n\5\r\5\16\5#\3\6"+
		"\3\6\6\6(\n\6\r\6\16\6)\3\7\3\7\5\7.\n\7\3\7\6\7\61\n\7\r\7\16\7\62\3"+
		"\b\6\b\66\n\b\r\b\16\b\67\3\b\3\b\6\b<\n\b\r\b\16\b=\5\b@\n\b\3\b\5\b"+
		"C\n\b\3\b\6\bF\n\b\r\b\16\bG\3\b\3\b\6\bL\n\b\r\b\16\bM\5\bP\n\b\3\b\3"+
		"\b\6\bT\n\b\r\b\16\bU\3\b\5\bY\n\b\5\b[\n\b\3\t\3\t\3\t\7\t`\n\t\f\t\16"+
		"\tc\13\t\3\n\3\n\3\n\3\n\6\ni\n\n\r\n\16\nj\3\n\3\n\3\13\6\13p\n\13\r"+
		"\13\16\13q\3\13\3\13\2\2\f\3\2\5\2\7\2\t\2\13\2\r\2\17\3\21\4\23\5\25"+
		"\6\3\2\n\3\2c|\3\2\62;\4\2--//\3\2gg\3\2\60\60\4\2GGgg\3\2))\5\2\13\f"+
		"\17\17\"\"\2\u0083\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2"+
		"\3\27\3\2\2\2\5\31\3\2\2\2\7\34\3\2\2\2\t\36\3\2\2\2\13%\3\2\2\2\r+\3"+
		"\2\2\2\17Z\3\2\2\2\21\\\3\2\2\2\23d\3\2\2\2\25o\3\2\2\2\27\30\t\2\2\2"+
		"\30\4\3\2\2\2\31\32\t\3\2\2\32\6\3\2\2\2\33\35\t\4\2\2\34\33\3\2\2\2\34"+
		"\35\3\2\2\2\35\b\3\2\2\2\36\37\t\5\2\2\37!\5\7\4\2 \"\5\5\3\2! \3\2\2"+
		"\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\n\3\2\2\2%\'\t\6\2\2&(\5\5\3\2\'&\3"+
		"\2\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\f\3\2\2\2+-\t\7\2\2,.\t\4\2\2-"+
		",\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/\61\t\3\2\2\60/\3\2\2\2\61\62\3\2\2\2"+
		"\62\60\3\2\2\2\62\63\3\2\2\2\63\16\3\2\2\2\64\66\t\3\2\2\65\64\3\2\2\2"+
		"\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\289\3\2\2\29?\7\60\2\2:<\t\3\2"+
		"\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>@\3\2\2\2?;\3\2\2\2?@\3\2\2"+
		"\2@B\3\2\2\2AC\5\r\7\2BA\3\2\2\2BC\3\2\2\2C[\3\2\2\2DF\t\3\2\2ED\3\2\2"+
		"\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2\2\2I[\5\r\7\2JL\t\3\2\2KJ\3\2\2"+
		"\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2OK\3\2\2\2OP\3\2\2\2PQ\3\2\2"+
		"\2QS\7\60\2\2RT\t\3\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2"+
		"\2\2WY\5\r\7\2XW\3\2\2\2XY\3\2\2\2Y[\3\2\2\2Z\65\3\2\2\2ZE\3\2\2\2ZO\3"+
		"\2\2\2[\20\3\2\2\2\\a\5\3\2\2]`\5\3\2\2^`\5\5\3\2_]\3\2\2\2_^\3\2\2\2"+
		"`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\22\3\2\2\2ca\3\2\2\2dh\7)\2\2ei\n\b\2"+
		"\2fg\7)\2\2gi\7)\2\2he\3\2\2\2hf\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2"+
		"kl\3\2\2\2lm\7)\2\2m\24\3\2\2\2np\t\t\2\2on\3\2\2\2pq\3\2\2\2qo\3\2\2"+
		"\2qr\3\2\2\2rs\3\2\2\2st\b\13\2\2t\26\3\2\2\2\27\2\34#)-\62\67=?BGMOU"+
		"XZ_ahjq\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}