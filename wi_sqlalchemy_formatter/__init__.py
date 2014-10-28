import logging
import sqlparse

from MySQLdb.converters import conversions, escape
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers import get_lexer_by_name
from sqlalchemy.sql import compiler


def compile_query(query):
    """
    Compile sqlalchemy query object to regular SQL with escaped values
    @param query: sqlalchemy query object
    @return: string
    """
    dialect = query.session.bind.dialect
    statement = query.statement
    comp = compiler.SQLCompiler(dialect, statement)
    enc = dialect.encoding
    params = []
    for k in comp.positiontup:
        v = comp.params[k]
        if isinstance(v, unicode):
            v = v.encode(enc)
        params.append(escape(v, conversions))
    return (comp.string.encode(enc) % tuple(params)).decode(enc)


def color_sql(code):
    """
    Beautify and colorify SQL snippet.
    @param code: string
    @return: string
    """

    lexer = get_lexer_by_name("sql", stripall=True)
    sql = sqlparse.format(code, reindent=True, keyword_case='upper')
    return highlight(sql, lexer, TerminalFormatter())


def color_q(query_object):
    """
    Beautify and colorify sqlalchemy query object.
    @param query_object: sqlalchemy query object
    @return: string
    """
    return color_sql(compile_query(query_object))

python_lexer = get_lexer_by_name("python", stripall=True)


class SqlAlchemyFormatter(logging.Formatter):
    """Pygments-powered logging formatter for SQLAlchemy, try it like this:

    [formatter_sqlalchemy]
    class = wi_sqlalchemy_formatter.SqlAlchemyFormatter
    format = %(levelname)s %(message)s

    and you'll be amazed. SQLs formatted, highlighted, with values.

    This is WIP, works for now, but might break.
    """
    previous_record = None

    def format(self, record):
        if '%r' in record.msg:  # what does this mean?
            if record.levelname == 'INFO' and self.previous_record:
                # Let's fill what we saved with values
                # I'm sure this will break sometimes.
                filler = record.args[0]
                if hasattr(filler, 'params'):
                    filler = filler.params
                complete = self.previous_record % filler
                self.previous_record = None
                return color_sql(complete)
            # sql alchemy debug row, it's not in python but looks best as
            # python
            return highlight(
                logging.Formatter.format(self, record),
                python_lexer,
                TerminalFormatter()
            )
        if record.levelname == 'INFO':
            # That is an SQL we need to fill with data in the next record.
            self.previous_record = record.msg
            return ''
