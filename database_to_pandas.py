import getpass
import pymysql
import unidecode
import pandas as pd
import tempfile
import subprocess
import sys

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_colwidth',500)

def generate_pdf(latexfile,
    pdf='output.pdf',
    dwld_dir='/home/restrepo/downloads',
    url_dir='file:///home/restrepo/downloads',id=None):
    """
    pdflatex upon latexfile to generate 'pdf'  file in 
    'dwld_dir' with browser link 'url_dir'
    """

    f=tempfile.NamedTemporaryFile('w',suffix='.tex',delete=False)
    f.write(latexfile)
    f.close()
    lo=subprocess.Popen('pdflatex {:s}'.format(f.name).split(),cwd='/tmp',
                        stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
    pdffile='{:s}'.format(f.name).split('.tex')[0]+'.pdf'
    if lo[0].decode('utf8').find(pdffile.split('/')[-1])>-1:
        
        kk=subprocess.Popen('mv {:s} {:s}/{:s}'.format(pdffile,dwld_dir,pdf).split()).communicate()
        print('output in {:s}/{:s}'.format(url_dir,pdf))
        for suffix in  ['.aux','.log','.out','.tex']:
            sc=subprocess.Popen( ['rm', '{:s}'.format(f.name).split('.tex')[0]+suffix] ).communicate()
    else:
        print(lo[0].decode('utf8'))
        sys.exit('LaTeX ERROR:')    
    return latexfile

class database_to_pandas(object):
    """
    Convert Data Base  to pondas and filtered index to Series and 
    define methods to use them.
    Intialize with choose_db and main_table to build attibute: choose_db[main_table]
    See for example:
    {'Diego_Restrepo':'cartas','cartas_gfif':'cartas','seminarios':'talks'}
    The optional aux_tables must be set to '' if not required, otherwise 
    'cartas_sign' is used
    """
    def __init__(self,choose_db='Diego_Restrepo',main_table='cartas',id=None,
                 aux_tables='cartas_sign',common_columns='signature',verbose=False):
        password=getpass.getpass()
        #TODO: read from config
        self.choose_db={choose_db:main_table}
        self.DataBase=choose_db
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd=password, db=choose_db)

        df=pd.read_sql('select * from {};'.format(self.choose_db[choose_db]), con=conn)

        #TODO: generilize to addtional tables
        if aux_tables:
            sg=pd.read_sql('select * from {};'.format(aux_tables), con=conn)


        conn.close()
        self.pandas_DataFrame=df
        #print(df.shape[0])
        #return df,sg
        if df.shape[0]:
            if not id:
                id=df.id.values[-1]
            self.pandas_Series=df[df.id==id].reset_index(drop=True).loc[0]
            if aux_tables:
                #TODO:
                self.pandas_Series['common_{}'.format(common_columns)]=sg[
                    sg[common_columns]==self.pandas_Series[common_columns]].reset_index(drop=True).loc[0,'sign']
            if verbose:
                print(self.pandas_Series)
        else:
            sys.exit('Error reading databases')
            return df

    
    def to_latex(self,func):
        '''Build a function to build the latex file with the self.Series keys
           and call it from here
        '''
        #TODO: check if class has methoed
        self.latexfile=func(self.pandas_Series)
        return self.latexfile
    #return generate_pdf(c)
    def to_pdf(self,func,**kwargs):
        '''Build a function to build the latex file with the self.Series keys
           and call it from here
        '''
        self.latexfile=func(self.pandas_Series)
        return generate_pdf(self.latexfile,**kwargs)
        
    def backup_database(self):
        '''
        Backup DB
        '''
    
        password=getpass.getpass()

        print('Trying to create backup file db_{:s}_backup.sql'.format( self.DataBase  )   )
        ok=subprocess.Popen('mysqldump -u root -p{:s} {:s} > db_{:s}_backup.sql'.format(
                         password,self.DataBase,self.DataBase),shell=True,
                         stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()

        print()

        return ok